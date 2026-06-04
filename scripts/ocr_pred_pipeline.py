import dotenv
import pandas as pd
import regex as re
from multiprocessing import freeze_support
from tqdm import tqdm

from zettelsortierung.DataTypes import Zettel, Classification, Label
from zettelsortierung import DataBase
from zettelsortierung import (
    Sammlungen,
    Classifiers,
)

dotenv.load_dotenv()


def print_res(results: list[Classification]):
    for classification in results:
        print(
            f"{classification.zettel.id}  ->  {classification.label.sammlung.name}\t\t({classification.classifier.name}, {classification.label.confidence*100:.2f})"  # type: ignore
        )
    return results


def search_ocr_results(pattern: re.Pattern, texts) -> list[Zettel]:
    scan_ids: list[str] = []
    for text in tqdm(texts):
        if len(re.findall(pattern, text[1])):
            scan_ids.append(text[0])

    zettels: list[Zettel] = []
    for scan_id in tqdm(scan_ids):
        path = db.get_full_path(scan_id)
        zettels.append(Zettel(path))

    return zettels


def make_ocr_classification(kreis: str, ort: str, texts):
    pattern = re.compile(rf"{kreis},? ?{ort}")
    hits = search_ocr_results(pattern, texts)
    classifications = []
    for hit in hits:
        classifications.append(
            Classification(
                zettel=hit,
                classifier=Classifiers.OCR,
                label=Label(
                    sammlung=Sammlungen[f"ANON_{kreis.upper()}_{ort.upper()}"],
                    confidence=1.0,
                ),
            )
        )
    return classifications


def ocr_based_classification():
    texts = db.get_ocr_concat()

    regions = pd.read_csv("data/processed/Orte.csv", sep="\t")
    kreis_ort_list = list(
        zip(regions["Kreis"].str.strip(), regions["Abkuerzung"].str.strip())
    )
    regions["Kreis"].unique()
    for kreis in regions["Kreis"].unique():
        kreis_ort_list.append((kreis, "Xy"))

    for kreis, ort in tqdm(kreis_ort_list):
        classifications = make_ocr_classification(kreis, ort, texts)
        print_res(classifications)
        db.merge_classifications(classifications)


if __name__ == "__main__":
    freeze_support()

    connection_string = "sqlite:////home/jan/Dokumente/IT-Beratung Raring/Zettelsortierung/data/interim/pre-zettel.db"
    db = DataBase(connection_string=connection_string)

    ocr_based_classification()
