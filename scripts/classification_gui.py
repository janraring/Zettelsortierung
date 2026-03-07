from functools import partial
from random import shuffle
from enum import Enum

from zettelsortierung.db import DataBase
from zettelsortierung.DataTypes import Classifiers, TopCategory, Zettel
from zettelsortierung.ClassificationGUI import run_classification

db = DataBase()


def get_stats() -> dict[str, int]:
    classifications = db.get_classifications(Classifiers.GOLD, TopCategory)
    counts: dict[str, int] = {cat.name: 0 for cat in TopCategory}
    counts["Total"] = len(classifications)
    for probs in classifications.values():
        for cat, prob in probs.items():
            if prob == 1.0:
                counts[cat.name] += 1
    return counts


def get_unclassified() -> list[Zettel]:
    already_done = db.get_classified_ids(Classifiers.GOLD, TopCategory)
    zettels = [z for z in db.get_zettel() if z.id not in already_done]
    shuffle(zettels)
    return zettels


def get_previous(label: Enum) -> list[Zettel]:
    classifications = db.get_classifications(Classifiers.GOLD, TopCategory)
    skipped_ids = {
        zid for zid, probs in classifications.items()
        if probs.get(label, 0.0) == 1.0
    }
    return db.get_zettel_by_ids(skipped_ids)


def main():
    queries = {
        'Unclassified': get_unclassified,
        'Skipped':      partial(get_previous, TopCategory.SKIP),
        'Lautschrift':  partial(get_previous, TopCategory.LAUTSCHRIFT),
        'Fragebogen':   partial(get_previous, TopCategory.FRAGEBOGEN),
        'Wortschatz':   partial(get_previous, TopCategory.WORTSCHATZ),
        'Sonstige':     partial(get_previous, TopCategory.SONSTIGE),
    }

    callback = partial(db.save_classification, Classifiers.GOLD)
    run_classification(queries, TopCategory, callback, get_stats)

if __name__ == '__main__':
    main()