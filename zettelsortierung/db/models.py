from sqlalchemy import Column, Integer, String, ForeignKey, Float
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


class BoundingBoxModel(Base):
    __tablename__ = "bounding_boxes"
    scan_id = Column(String, ForeignKey("scans.id"), primary_key=True)
    feature_id = Column(Integer, primary_key=True)
    x = Column(Integer)
    y = Column(Integer)
    w = Column(Integer)
    h = Column(Integer)


class OCRResultModel(Base):
    __tablename__ = "ocr_results"
    scan_id = Column(String, ForeignKey("scans.id"), primary_key=True)
    feature_id = Column(Integer, primary_key=True)
    text = Column(String)


class ClassificationModel(Base):
    __tablename__ = "classifications"
    zettel_id = Column(String, ForeignKey("zettel.id"), primary_key=True)
    scheme = Column(String, primary_key=True)
    classifier = Column(String, primary_key=True)
    label = Column(String, primary_key=True)
    probability = Column(Float, default=0.0)
