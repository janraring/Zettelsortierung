from functools import partial, cache
from enum import Enum
from tqdm import tqdm
from typing import Optional
from pathlib import Path
import regex as re
import os

from dotenv import load_dotenv
from PIL import Image
import torch

from zettelsortierung.db import DataBase
from zettelsortierung.DataTypes import Zettel
from zettelsortierung.ClassificationGUI import run_classification
from zettelsortierung.Sammlungen import Sammlungen, Classifiers
from zettelsortierung.nn import (
    MobileNetV3ModelSmall,
    TrainingConfig,
    ParquetDataset,
    mobile_net_infer_transform,
)

load_dotenv()
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
    zettel_ids = {
        zid for zid, label in classifications.items() if label.sammlung == sammlung
    }
    return db.get_zettels_by_ids(list(zettel_ids))


def get_random_sample(n: int = 100) -> list[Zettel]:
    sample = db.get_random_zettel(limit=n)
    predictions = {}
    for zettel in tqdm(sample):
        predictions[zettel] = get_predictions(zettel)
    sample.sort(key=lambda z: predictions[z][0][1], reverse=False)
    return sample


#####################################################################
# Predictions
#####################################################################


def load_model(path_str: str, config: TrainingConfig) -> MobileNetV3ModelSmall:
    path = Path(path_str)
    model = MobileNetV3ModelSmall(num_classes=config.num_classes)
    model.load_state_dict(
        torch.load(path / "model_weights.pt", map_location=config.device)
    )
    model.to(config.device)
    model.eval()
    return model


def predict(model, image: Image.Image, config: TrainingConfig) -> dict:
    tensor = mobile_net_infer_transform(image).unsqueeze(0).to(config.device)  # type: ignore

    with torch.no_grad():
        logits = model(tensor)
        probs = torch.softmax(logits, dim=1)
        probs = probs[0]

    confidence = probs.max().item()
    class_idx = probs.argmax().item()

    return {
        "class": class_idx,
        "confidence": confidence,
        "unknown": False,
        "all_probs": probs,
    }


root = os.getenv("PROJECT_ROOT")
dataset = ParquetDataset(f"{root}/data/interim/136_classes.parquet", train=False)
config = TrainingConfig(num_classes=len(dataset.get_classes()))
model = load_model(f"{root}/models/mobile_net_v3_small_30ep_on_136_classes", config)


def get_predictions(zettel: Zettel) -> list[tuple[str, float]]:
    # Return top 10 predictions
    results = predict(model, Image.open(zettel.recto.full_path), config)
    top_indices = torch.topk(results["all_probs"], k=10).indices.cpu().numpy()
    top_probs = results["all_probs"][top_indices].cpu().numpy()
    classes = dataset.get_classes()
    predictions = [(classes[idx], prob) for idx, prob in zip(top_indices, top_probs)]
    return predictions


def main():
    queries = {
        "0_Classified": partial(db.get_classified, Classifiers.MANUELL),
        "0_Unclassified": get_unclassified,
        "0_Random_Sample": partial(get_random_sample, n=100),
    }
    for sammlung in Sammlungen:
        queries[sammlung.name.title()] = partial(get_previously_classified, sammlung)

    sorted_queries = dict(sorted(queries.items()))

    run_classification(
        classes=Sammlungen,
        on_classify=partial(db.save_classification, classifier=Classifiers.MANUELL),
        search_ocr_results=search_ocr_results,
        get_status=get_status,
        get_stats=get_stats,
        get_predictions=get_predictions,
        queries=sorted_queries,
    )


if __name__ == "__main__":
    main()
