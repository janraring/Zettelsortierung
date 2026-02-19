import os
from sqlalchemy import Column, Integer, String, Table, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base#, relationship, backref

from zettelsortierung.DataTypes import Scan, Zettel, BoundingBox, DataPoint
from zettelsortierung.DataBase import *

from dotenv import load_dotenv
load_dotenv()


Base = declarative_base()


class ScanModel(Base):
    __tablename__ = 'scans'

    id = Column('id', String, primary_key=True)
    file_name = Column('file_name', String)
    relative_path = Column('relative_path', String)
    full_path = Column('full_path', String)

    def __init__(self, scan: Scan):
        self.id = scan.id
        self.file_name = scan.file_name
        self.relative_path = scan.relative_path
        self.full_path = scan.full_path

    def __repr__(self):
        return f'ScanModel({self.id}, {self.relative_path})'
    
    def to_domain(self) -> Scan:
        return Scan(self.full_path)


class ZettelModel(Base):
    __tablename__ = 'zettel'

    id = Column('id', String, primary_key=True)
    recto_id = Column('recto', String, ForeignKey('scans.id'))
    verso_id = Column('verso', String, ForeignKey('scans.id'))

    def __init__(self, zettel: Zettel):
        self.id = zettel.id
        self.recto_id = zettel.recto.id
        self.verso_id = zettel.verso.id
    
    def __repr__(self):
        return f'Zettel({self.id})'


class BoundingBoxModel(Base):
    __tablename__ = 'bounding_boxes'

    scan_id = Column('scan_id', String, ForeignKey('scans.id'), primary_key=True)
    feature_id = Column('feature_id', Integer, primary_key=True)
    x = Column('x', Integer)
    y = Column('y', Integer)
    w = Column('w', Integer)
    h = Column('h', Integer)

    def __init__(self, dp: DataPoint):
        self.scan_id = dp.scan.id
        self.id = dp.feature_id
        self.x, self.y, self.w, self.h = dp.feature


class OCRResultModel(Base):
    __tablename__ = 'ocr_results'

    scan_id = Column('scan_id', String, ForeignKey('scans.id'), primary_key=True)
    feature_id = Column('feature_id', Integer, ForeignKey('bounding_boxes.feature_id'), primary_key=True)
    text = Column('text', String)

    def __init__(self, dp: DataPoint):
        self.scan_id = dp.scan.id
        self.id = dp.feature_id
        self.text = dp.feature



connection_string = os.getenv('DATABASE_CONNECTION_STRING')
engine = create_engine(connection_string)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_scan_list(scans: list[Scan]):
    counter = 0
    for scan in scans:
        scan_model = ScanModel(Scan(scan))
        session.add(scan_model)

        counter += 1
        if counter % 10000 == 0:
            session.commit()
            print(counter)
    else:
        session.commit()
        print(counter)

def add_scan(scan: Scan):
    scan_model = ScanModel(scan)
    session.add(scan_model)
    session.commit()

def get_scans():
    return session.query(ScanModel).all()
