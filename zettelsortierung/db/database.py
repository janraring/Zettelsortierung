from collections import Counter
from enum import Enum
import os
from typing import Sequence

import dotenv
from sqlalchemy import create_engine, exists, func, select, update
from sqlalchemy.orm import sessionmaker
from tqdm import tqdm

from zettelsortierung.DataTypes import Classification, Label, Probe, Scan, Zettel
from zettelsortierung.db.models import (
    Base,
    ClassificationModel,
    ClassifierModel,
    ClassModel,
    KreisModel,
    LandschaftModel,
    OCRResultModel,
    OrtModel,
    ScanModel,
    SourceModel,
    ZettelModel,
)
from zettelsortierung.Sammlungen import Sammlungen

dotenv.load_dotenv()


class DataBase:
    def __init__(self, connection_string: str | None = None, echo: bool = False):
        if connection_string is None:
            connection_string = os.getenv("DATABASE_CONNECTION_STRING")
        if connection_string is None:
            raise ValueError("No connection string provided")

        self.engine = create_engine(connection_string, echo=echo)
        Base.metadata.create_all(bind=self.engine)
        self._Session = sessionmaker(bind=self.engine)
        self.session = self._Session()

    # ---- generic bulk helper ----

    def _bulk_add(self, items, batch_size: int = 10000) -> None:
        i = 0
        for i, item in enumerate(items, 1):
            self.session.add(item)
            if i % batch_size == 0:
                self.session.commit()
                print(f"Added {i} elements")
        self.session.commit()
        print(f"Done: {i} items added")

    def _bulk_merge(self, items, batch_size: int = 10000) -> None:
        i = 0
        for i, item in enumerate(items, 1):
            self.session.merge(item)
            if i % batch_size == 0:
                self.session.commit()
                print(f"Merged {i} elements")
        self.session.commit()
        print(f"Done: {i} items merged")

    # ---- Scans ----

    def add_scans(self, scans: list[Scan]) -> None:
        self._bulk_add(
            ScanModel(
                id=scan.id,
                file_name=scan.file_name,
                relative_path=scan.relative_path,
                full_path=scan.full_path,
            )
            for scan in scans
        )

    def get_scans(self) -> list[Scan]:
        rows = self.session.query(ScanModel).all()
        return [Scan(str(row.full_path)) for row in rows]

    # ---- Zettel ----

    def add_zettel(self, zettels: list[Zettel]) -> None:
        self._bulk_add(
            ZettelModel(id=zettel.id, recto_id=zettel.recto.id, verso_id=zettel.verso.id)
            for zettel in zettels
        )

    def get_zettel(self, limit: int | None = None) -> list[Zettel]:
        rows = (
            self.session.query(ZettelModel, ScanModel.full_path)
            .join(ScanModel, ZettelModel.recto_id == ScanModel.id)
            .limit(limit)
            .all()
        )
        return [Zettel(full_path) for _, full_path in tqdm(rows)]

    def get_random_zettel(self, limit: int = 1000) -> list[Zettel]:
        rows = (
            self.session.query(ZettelModel, ScanModel.full_path)
            .join(ScanModel, ZettelModel.recto_id == ScanModel.id)
            .order_by(func.random())
            .limit(limit)
            .all()
        )
        return [Zettel(full_path) for _, full_path in rows]

    def get_zettels_by_ids(self, ids: list[str]) -> list[Zettel]:
        from itertools import islice

        results = []
        it = iter(ids)
        while chunk := list(islice(it, 999)):
            rows = (
                self.session.query(ZettelModel, ScanModel.full_path)
                .join(ScanModel, ZettelModel.recto_id == ScanModel.id)
                .where(ZettelModel.id.in_(chunk))
                .all()
            )
            results.extend(Zettel(full_path) for _, full_path in rows)
        return results

    def update_lemmas(self, lemmas: dict[str, str], batch_size: int = 10000) -> None:
        i = 0
        for i, (zettel_id, lemma) in enumerate(lemmas.items(), 1):
            self.session.execute(
                update(ZettelModel).where(ZettelModel.id == zettel_id).values(lemma=lemma)
            )
            if i % batch_size == 0:
                self.session.commit()
                print(f"Updated {i} lemmas")
        self.session.commit()
        print(f"Done: {i} lemmas updated")

    def get_zettels_by_ids_old(self, ids: list[str]) -> list[Zettel]:
        rows = (
            self.session.query(ZettelModel, ScanModel.full_path)
            .join(ScanModel, ZettelModel.recto_id == ScanModel.id)
            .where(ZettelModel.id.in_(ids))
            .all()
        )
        return [Zettel(full_path) for _, full_path in rows]

    # ---- Geography ----

    def add_landschaften(self, landschaften: list[tuple[str, str, str]]) -> None:
        for abbr, name, desc in landschaften:
            self.session.add(LandschaftModel(abbreviation=abbr, name=name, description=desc))
        self.session.commit()

    def add_kreise(self, kreise: list[tuple[str, str]]) -> None:
        for abbr, name in kreise:
            self.session.add(KreisModel(abbreviation=abbr, name=name))
        self.session.commit()

    def add_orte(self, orte: list[tuple[str, str, str]]) -> None:
        for kreis, abbr, name in orte:
            self.session.add(OrtModel(kreis=kreis, abbreviation=abbr, name=name))
        self.session.commit()

    def add_source(self, sources: list[tuple[str, str]]) -> None:
        self._bulk_add(
            SourceModel(sigle=sigle, description=description) for sigle, description in sources
        )

    # ---- Bounding Boxes & OCR ----

    def add_bounding_boxes(self, probe: Probe) -> None:
        self._bulk_add(
            OCRResultModel(
                scan_id=dp.scan.id,
                feature_id=dp.feature_id,
                x=int(dp.feature[0]),
                y=int(dp.feature[1]),
                w=int(dp.feature[2]),
                h=int(dp.feature[3]),
                text=dp.feature[4],
            )
            for dp in probe
        )

    # ---- Classifiers ----

    def merge_classifiers(self, classifiers: type[Enum]) -> None:
        self._bulk_merge(
            ClassifierModel(name=classifier.name, description=classifier.value.description)
            for classifier in classifiers
        )

    # ---- Classes ----

    def merge_classes(self, classes: type[Enum]) -> None:
        self._bulk_merge(
            ClassModel(
                name=cls.name,
                trace=cls.value.trace,
                groups=cls.value.groups,
                sigle=cls.value.sigle,
                description=cls.value.description,
                landschaft=cls.value.landschaft,
                kreis=cls.value.kreis,
                ort=cls.value.ort,
            )
            for cls in classes
        )

    # ---- Classifications ----

    def merge_classifications(self, classifications: list[Classification]) -> None:
        self._bulk_merge(
            ClassificationModel(
                zettel_id=c.zettel.id,
                classifier=c.classifier.name,
                label=c.label.sammlung.name,
                confidence=c.label.confidence,
            )
            for c in classifications
        )

    def save_classification(self, zettel: Zettel, label: Label, classifier: Enum) -> None:
        """Save a single classification — used as GUI callback."""
        self.session.merge(
            ClassificationModel(
                zettel_id=zettel.id,
                classifier=classifier.name,
                label=label.sammlung.name,
                confidence=label.confidence,
            )
        )
        self.session.commit()

    def get_classified(self, classifier: Enum) -> list[Zettel]:
        """Return already-classified zettel (for resuming)."""
        stmt = (
            select(ClassificationModel.zettel_id)
            .where(ClassificationModel.classifier == classifier.name)
            .distinct()
        )
        result_ids = set(self.session.execute(stmt).scalars().all())
        return self.get_zettels_by_ids(list(result_ids))

    def get_classifications(self, classifier: Enum) -> dict[str, Label]:
        """Load all classifications back as {zettel_id: label}."""
        rows = (
            self.session.query(ClassificationModel)
            .filter(ClassificationModel.classifier == classifier.name)
            .all()
        )
        result: dict[str, Label] = {}
        for row in rows:
            label = Label(Sammlungen[str(row.label)], row.confidence)  # type: ignore
            result[str(row.zettel_id)] = label
        return result

    def filter_classifications(
        self, classifier: Enum, class_label: Enum, min_conf: float = 0.0
    ) -> dict[str, Label]:
        """Load all zettels classified as `label` by `classifier` as {zettel_id: label}."""
        rows = (
            self.session.query(ClassificationModel)
            .filter(ClassificationModel.classifier == classifier.name)
            .filter(ClassificationModel.label == class_label.name)
            .filter(ClassificationModel.confidence >= min_conf)
            .all()
        )
        result: dict[str, Label] = {}
        for row in rows:
            label = Label(Sammlungen[str(row.label)], row.confidence)  # type: ignore
            result[str(row.zettel_id)] = label
        return result

    def get_predicted_label(self, zettel: Zettel, classifier: Enum) -> Label | None:
        """Return the label with the highest probability."""
        stmt = (
            select(ClassificationModel.label, ClassificationModel.confidence)
            .where(ClassificationModel.zettel_id == zettel.id)
            .where(ClassificationModel.classifier == classifier.name)
            .order_by(ClassificationModel.confidence.desc())
            .limit(1)
        )
        label = self.session.execute(stmt).one()
        return Label(Sammlungen[label[0]], label[1]) if label else None

    # ---- Queries ----

    def get_missing_ocrs(self) -> Sequence[str]:
        stmt = (
            select(ScanModel.full_path)
            .where(~exists().where(OCRResultModel.scan_id == ScanModel.id))
            .where(ScanModel.id.endswith("_1"))
        )
        return self.session.execute(stmt).scalars().all()

    def get_full_path(self, scan_id: str) -> str:
        stmt = select(ScanModel.full_path).where(ScanModel.id == scan_id)
        return self.session.execute(stmt).scalars().all()[0]

    def get_ocr_concat(self):
        stmt = select(
            OCRResultModel.scan_id,
            func.group_concat(OCRResultModel.text, " | ").label("combined_text"),
        ).group_by(OCRResultModel.scan_id)
        return self.session.execute(stmt).all()

    def get_label_counts(self, classifier: Enum | None = None) -> Counter:
        query = self.session.query(ClassificationModel.label, func.count().label("n"))
        if classifier is not None:
            query = query.filter(ClassificationModel.classifier == classifier.value.title)
        rows = query.group_by(ClassificationModel.label).all()
        return Counter({label: n for label, n in rows})
