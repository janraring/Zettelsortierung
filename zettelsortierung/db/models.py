from sqlalchemy import Column, Integer, String, ForeignKey, Float, ForeignKeyConstraint
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ScanModel(Base):
    __tablename__ = "scans"
    id = Column(String, primary_key=True)
    file_name = Column(String)
    relative_path = Column(String)
    full_path = Column(String)


class ZettelModel(Base):
    __tablename__ = "zettel"
    id = Column(String, primary_key=True)
    lemma = Column(String)
    recto_id = Column(String, ForeignKey("scans.id"))
    verso_id = Column(String, ForeignKey("scans.id"))


class LandschaftModel(Base):
    __tablename__ = "landschaften"
    abbreviation = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)


class KreisModel(Base):
    __tablename__ = "kreise"
    abbreviation = Column(String, primary_key=True)
    name = Column(String)


class OrtModel(Base):
    __tablename__ = "orte"
    kreis = Column(String, ForeignKey("kreise.abbreviation"), primary_key=True)
    abbreviation = Column(String, primary_key=True)
    name = Column(String)


class SourceModel(Base):
    __tablename__ = "sources"
    sigle = Column(String, primary_key=True)
    description = Column(String)


class OCRResultModel(Base):
    __tablename__ = "ocr_results"
    scan_id = Column(String, ForeignKey("scans.id"), primary_key=True)
    feature_id = Column(Integer, primary_key=True)
    x = Column(Integer)
    y = Column(Integer)
    w = Column(Integer)
    h = Column(Integer)
    text = Column(String)


class ClassificationModel(Base):
    __tablename__ = "classifications"
    zettel_id = Column(String, ForeignKey("zettel.id"), primary_key=True)
    classifier = Column(String, ForeignKey("classifiers.name"), primary_key=True)
    label = Column(String, ForeignKey("classes.name"))
    confidence = Column(Float, default=0.0)


class ClassifierModel(Base):
    __tablename__ = "classifiers"
    name = Column(String, primary_key=True)
    description = Column(String)


class ClassModel(Base):
    __tablename__ = "classes"
    name = Column(String, primary_key=True)
    trace = Column(String)
    groups = Column(String)
    sigle = Column(String, ForeignKey("sources.sigle"))
    description = Column(String)
    landschaft = Column(String, ForeignKey("landschaften.abbreviation"))
    kreis = Column(String, ForeignKey("kreise.abbreviation"))
    ort = Column(String)

    __table_args__ = (
        ForeignKeyConstraint(["kreis", "ort"], ["orte.kreis", "orte.abbreviation"]),
    )
