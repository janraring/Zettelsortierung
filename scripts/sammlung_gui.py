from functools import partial, cache
from enum import Enum
from tqdm import tqdm
from typing import Optional
import regex as re

from zettelsortierung.db import DataBase
from zettelsortierung.DataTypes import Zettel
from zettelsortierung.ClassificationGUI import run_classification
from zettelsortierung.Sammlungen import Sammlungen, Classifiers

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


def main():
    queries = {
        "0_Classified": partial(db.get_classified, Classifiers.MANUELL),
        "0_Unclassified": get_unclassified,
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
        queries=sorted_queries,
    )


if __name__ == "__main__":
    main()
