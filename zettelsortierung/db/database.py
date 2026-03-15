# pyright: reportArgumentType=false

import os
from typing import Sequence
from enum import Enum
from tqdm import tqdm

from sqlalchemy import create_engine, select, exists, func
from sqlalchemy.orm import sessionmaker

from zettelsortierung.DataTypes import Scan, Zettel, DataPoint, Probe
from zettelsortierung.Sammlungen import Sammlungen, Label
from zettelsortierung.db.models import (
    Base,
    ScanModel,
    ZettelModel,
    LandschaftModel,
    KreisModel,
    OrtModel,
    BoundingBoxModel,
    OCRResultModel,
    ClassificationModel,
)

from dotenv import load_dotenv

load_dotenv()


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
                print(i)
        self.session.commit()
        print(f"Done: {i} items")

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
        return [Scan(row.full_path) for row in rows]

    # ---- Zettel ----

    def add_zettel(self, zettels: list[Zettel]) -> None:
        self._bulk_add(
            ZettelModel(
                id=zettel.id, recto_id=zettel.recto.id, verso_id=zettel.verso.id
            )
            for zettel in zettels
        )

    def get_zettel(self) -> list[Zettel]:
        rows = (
            self.session.query(ZettelModel, ScanModel.full_path)
            .join(ScanModel, ZettelModel.recto_id == ScanModel.id)
            .all()
        )
        return [Zettel(full_path) for _, full_path in tqdm(rows)]

    def get_zettels_by_ids(self, ids: set[str]) -> list[Zettel]:
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
            self.session.add(
                LandschaftModel(abbreviation=abbr, name=name, description=desc)
            )
        self.session.commit()

    def add_kreise(self, kreise: list[tuple[str, str]]) -> None:
        for abbr, name in kreise:
            self.session.add(KreisModel(abbreviation=abbr, name=name))
        self.session.commit()

    def add_orte(self, orte: list[tuple[str, str, str]]) -> None:
        for kreis, abbr, name in orte:
            self.session.add(OrtModel(kreis=kreis, abbreviation=abbr, name=name))
        self.session.commit()

    # ---- Bounding Boxes & OCR ----

    def add_bounding_boxes(self, probe: Probe) -> None:
        self._bulk_add(
            BoundingBoxModel(
                scan_id=dp.scan.id,
                feature_id=dp.feature_id,
                x=int(dp.feature[0]),
                y=int(dp.feature[1]),
                w=int(dp.feature[2]),
                h=int(dp.feature[3]),
            )
            for dp in probe
        )

    def add_ocr_results(self, probe: Probe) -> None:
        self._bulk_add(
            OCRResultModel(
                scan_id=dp.scan.id, feature_id=dp.feature_id, text=dp.feature
            )
            for dp in probe
        )

    # ---- Classifications ----

    def save_classification(
        self, zettel: Zettel, label: Label, classifier: Enum
    ) -> None:
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
        return self.get_zettels_by_ids(result_ids)

    #    def get_classified_ids(self, classifier: Enum, enum_class: type[Enum]) -> set[str]:
    #        """Return already-classified zettel IDs (for resuming)."""
    #        stmt = (
    #            select(ClassificationModel.zettel_id)
    #            .where(ClassificationModel.scheme == enum_class.__name__)
    #            .where(ClassificationModel.classifier == classifier.value)
    #            .distinct()
    #        )
    #        return set(self.session.execute(stmt).scalars().all())

    def get_classifications(self, classifier: Enum) -> dict[str, Label]:
        """Load all classifications back as {zettel_id: label}."""
        rows = (
            self.session.query(ClassificationModel)
            .filter(ClassificationModel.classifier == classifier.name)
            .all()
        )
        result: dict[str, Label] = {}
        for row in rows:
            label = Label(Sammlungen[row.label], row.confidence)
            result[row.zettel_id] = label
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
