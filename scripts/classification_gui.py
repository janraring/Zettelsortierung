from functools import partial, cache
from enum import Enum
from tqdm import tqdm
from typing import Optional
import regex as re

from zettelsortierung.db import DataBase
from zettelsortierung.DataTypes import Classifiers, TopCategory, Zettel
from zettelsortierung.ClassificationGUI import run_classification

db = DataBase()


@cache
def get_ocr_texts():
    return db.get_ocr_concat()


def get_stats() -> dict[str, int]:
    classifications = db.get_classifications(Classifiers.GOLD, TopCategory)
    counts: dict[str, int] = {cat.name: 0 for cat in TopCategory}
    counts["Total"] = len(classifications)
    for probs in classifications.values():
        for cat, prob in probs.items():
            if prob == 1.0:
                counts[cat.name] += 1
    return counts


def get_classified() -> list[Zettel]:
    return db.get_classified_zettels(Classifiers.GOLD, TopCategory)


def get_unclassified() -> list[Zettel]:
    already_done = db.get_classified_ids(Classifiers.GOLD, TopCategory)
    zettels = [z for z in db.get_zettel() if z.id not in already_done]
    return zettels


def get_previously_classified(label: Enum) -> list[Zettel]:
    classifications = db.get_classifications(Classifiers.GOLD, TopCategory)
    skipped_ids = {
        zid for zid, probs in classifications.items()
        if probs.get(label, 0.0) == 1.0
    }
    return db.get_zettels_by_ids(skipped_ids)


def get_status(zettel: Zettel) -> bool:
    classified = db.get_classified_zettels(Classifiers.GOLD, TopCategory)
    return zettel in classified


def generate_pattern(word: str):
    pattern = r''
    for i in range(len(word)):
        pattern += word[:i] + r'.' + word[i+1:] + '|'
    for i in range(1, len(word)):
        pattern += word[:i] + r'.' + word[i:] + '|'
    for i in range(1, len(word)-1):
        pattern += word[:i] + word[i+1:] + '|'
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
        path  = db.get_full_path(scan_id)
        zettels.append(Zettel(path))

    return zettels


def main():
    queries = {
        'Unclassified': get_unclassified,
        'Classified':   get_classified,
        'Skipped':      partial(get_previously_classified, TopCategory.SKIP),
        'Lautschrift':  partial(get_previously_classified, TopCategory.LAUTSCHRIFT),
        'Fragebogen':   partial(get_previously_classified, TopCategory.FRAGEBOGEN),
        'Wortschatz':   partial(get_previously_classified, TopCategory.WORTSCHATZ),
        'Sonstige':     partial(get_previously_classified, TopCategory.SONSTIGE),
    }

    print(db.get_zettels_by_ids({'T11-00726531'})[0].recto.full_path)
    callback = partial(db.save_classification, Classifiers.GOLD)
    run_classification(queries, TopCategory, callback, get_stats, search_ocr_results, get_status)


if __name__ == '__main__':
    main()