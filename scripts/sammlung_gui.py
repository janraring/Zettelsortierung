from enum import Enum
from functools import cache, partial
import os
from typing import Optional

import dotenv
from PIL import Image
import regex as re
import torch
from tqdm import tqdm
from zettelsortierung import Classifiers, DataBase, Label, Sammlungen, Zettel
from zettelsortierung.ClassificationGUI import run_classification
from zettelsortierung.nn import MobileNetV3ModelSmall, ParquetDataset

dotenv.load_dotenv()
db = DataBase()


#####################################################################
# Searching the OCR results
#####################################################################


@cache
def get_ocr_texts():
    return db.get_ocr_concat()


def generate_pattern(word: str):
    pattern = r""
    for i in range(len(word)):
        pattern += word[:i] + r"." + word[i + 1 :] + "|"
    for i in range(1, len(word)):
        pattern += word[:i] + r"." + word[i:] + "|"
    for i in range(1, len(word) - 1):
        pattern += word[:i] + word[i + 1 :] + "|"
    return pattern[:-1]


def search_ocr_results(input: str, fuzzy: Optional[bool] = False) -> list[Zettel]:
    if fuzzy:
        pattern = generate_pattern(input)
    else:
        pattern = input
    texts = get_ocr_texts()

    scan_ids: list[str] = []
    for text in tqdm(texts):
        if len(re.findall(pattern, text[1])):
            scan_ids.append(text[0])

    zettels: list[Zettel] = []
    for scan_id in tqdm(scan_ids):
        path = db.get_full_path(scan_id)
        zettels.append(Zettel(path))

    return zettels


#####################################################################
# Stats and Status
#####################################################################


def get_stats() -> dict[str, int]:
    classifications = db.get_classifications(Classifiers.MANUELL)
    counts: dict[str, int] = {sammlung.name: 0 for sammlung in Sammlungen}
    counts["Total"] = len(classifications)
    for label in classifications.values():
        counts[label.sammlung.name] += 1
    return counts


def get_status(zettel: Zettel) -> bool:
    classified = db.get_classified(Classifiers.MANUELL)
    return zettel in classified


#####################################################################
# Queries
#####################################################################


def get_unclassified() -> list[Zettel]:
    already_done = set(db.get_classified(Classifiers.MANUELL))
    all_zettels = set(db.get_zettel())
    unclassified = list(all_zettels - already_done)
    return unclassified


def get_previously_classified(sammlung: Enum) -> list[Zettel]:
    classifications = db.get_classifications(Classifiers.MANUELL)
    zettel_ids = {zid for zid, label in classifications.items() if label.sammlung == sammlung}
    return db.get_zettels_by_ids(list(zettel_ids))


def filter_model_classifications(
    sammlung: Enum, classifier: Enum, confidence: float = 0.0
) -> list[Zettel]:
    classifications = db.filter_classifications(sammlung, classifier, confidence)
    ids = list(classifications.keys())
    return db.get_zettels_by_ids(ids)


def get_random_sample(model, classes, n: int = 10000) -> list[Zettel]:
    sample = db.get_random_zettel(limit=n)
    predictions = {}
    for zettel in tqdm(sample):
        predictions[zettel] = get_predictions(model, classes, zettel)
    sample.sort(key=lambda z: predictions[z][0][1], reverse=False)
    return sample


#####################################################################
# Predictions
#####################################################################


def get_predictions_old(
    model: MobileNetV3ModelSmall, classes: list[str], zettel: Zettel
) -> list[tuple[str, float]]:
    K = 10  # number of predictions to return
    results = model.predict([Image.open(zettel.recto.full_path)])[0]
    top_indices = torch.topk(results["all_probs"], k=K).indices.cpu().numpy()
    top_probs = results["all_probs"][top_indices].cpu().numpy()
    predictions = [(classes[idx], prob) for idx, prob in zip(top_indices, top_probs)]
    return predictions


def get_predictions(
    model: MobileNetV3ModelSmall, classes: list[str], zettel: Zettel
) -> list[Label]:
    K = 10  # number of predictions to return
    results = model.predict([Image.open(zettel.recto.full_path)])[0]
    top_indices = torch.topk(results["all_probs"], k=K).indices.cpu().numpy()
    top_probs = results["all_probs"][top_indices].cpu().numpy()
    predictions = [
        Label(Sammlungen[classes[idx]], prob) for idx, prob in zip(top_indices, top_probs)
    ]
    return predictions


def main():
    num_classes = 581
    num_epochs = 60
    root = os.getenv("PROJECT_ROOT")

    dataset = ParquetDataset(f"{root}/data/interim/{num_classes}_classes.parquet", train=True)
    model = MobileNetV3ModelSmall.from_pretrained(
        path_str=f"{root}/models/mobile_net_v3_small_{num_classes}_classes_{num_epochs}_epochs_best",
        num_classes=num_classes,
    )
    classes = dataset.get_classes()

    queries = {
        "Classified": partial(db.get_classified, Classifiers.MANUELL),
        "Unclassified": get_unclassified,
        "Random": partial(get_random_sample, model, classes),
        "Filter": filter_model_classifications,
    }
    sorted_queries = dict(sorted(queries.items()))

    run_classification(
        classes=Sammlungen,
        on_classify=partial(db.save_classification, classifier=Classifiers.MANUELL),
        search_ocr_results=search_ocr_results,
        get_status=get_status,
        get_stats=get_stats,
        get_predictions=partial(get_predictions, model, classes),
        queries=sorted_queries,
    )


if __name__ in {"__main__", "__main_mp__"}:
    main()
