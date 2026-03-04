import os
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, select, exists, func
from sqlalchemy.orm import sessionmaker, declarative_base

from zettelsortierung.DataTypes import Scan, Zettel, DataPoint, Probe

from dotenv import load_dotenv
load_dotenv()


#####################################################################
# Base
#####################################################################

Base = declarative_base()


#####################################################################
# Physical Entities
#####################################################################

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


#####################################################################
# Geographical Entities
#####################################################################

class LandschaftModel(Base):
    __tablename__ = 'landschaften'

    abbreviation = Column('abbreviation', String, primary_key=True)
    name = Column('name', String)
    description = Column('description', String)

    def __init__(self,
                 abbreviation: str,
                 name: str,
                 description: str):
        self.abbreviation = abbreviation
        self.name = name
        self.description = description


class KreisModel(Base):
    __tablename__ = 'kreise'

    abbreviation = Column('abbreviation', String, primary_key=True)
    name = Column('name', String)

    def __init__(self, abbreviation: str, name: str):
        self.abbreviation = abbreviation
        self.name = name


class OrtModel(Base):
    __tablename__ = 'orte'

    kreis = Column('kreis', String, ForeignKey('kreise.abbreviation'), primary_key=True)
    abbreviation = Column('abbreviation', String, primary_key=True)
    name = Column('name', String)

    def __init__(self, kreis: str, abbreviation: str, name: str):
        self.kreis = kreis
        self.abbreviation = abbreviation
        self.name = name


#####################################################################
# Artefacts
#####################################################################

class BoundingBoxModel(Base):
    __tablename__ = 'bounding_boxes'

    scan_id = Column('scan_id',
                     String,
                     ForeignKey('scans.id'),
                     primary_key=True)
    feature_id = Column('feature_id', Integer, primary_key=True)
    x = Column('x', Integer)
    y = Column('y', Integer)
    w = Column('w', Integer)
    h = Column('h', Integer)

    def __init__(self, dp: DataPoint):
        self.scan_id = dp.scan.id
        self.feature_id = dp.feature_id
        self.x = int(dp.feature[0])
        self.y = int(dp.feature[1])
        self.w = int(dp.feature[2])
        self.h = int(dp.feature[3])


class OCRResultModel(Base):
    __tablename__ = 'ocr_results'

    scan_id = Column('scan_id',
                     String,
                     ForeignKey('scans.id'),
                     primary_key=True)
    feature_id = Column('feature_id',
                        Integer,
                        ForeignKey('bounding_boxes.feature_id'),
                        primary_key=True)
    text = Column('text', String)

    def __init__(self, dp: DataPoint):
        self.scan_id = dp.scan.id
        self.feature_id = dp.feature_id
        self.text = dp.feature

'''
#####################################################################
# Classifications
#####################################################################

class CategoryModel(Base):
    __tablename__ = 'category'

    category = Column('category', String, primary_key=True)
    top_category = Column('top_category', String)
    kreis = Column('kreis', String)
    ort = Column('ort', String)
    # Lautschrift
    #   - Untersammlungen (z.B. Gütersloh Wix)
    # Fragebogen
    #   - Reihe (z.B. Baader)
    # Wortschatz
    #   - Autor (z.B. Dittmar)
    # Aus Quelle
    #   - die Quelle (z.B. WmWb)
    # Sonstige
    #   - z.B. Verweis


class OCRClassification(Base):
    __tablename__ = 'ocr_classifications'

    zettel_id = Column('zettel_id', String, ForeignKey('zettel.id'), primary_key=True)
    category = Column('category', String)
    subcategory = Column('subcategory', String)
'''


#####################################################################
# Database Interaction
#####################################################################

class DataBase():
    def __init__(self,
                 connection_string: str = None,
                 echo: bool = False):
        if connection_string is None:
            connection_string = \
                os.getenv('DATABASE_CONNECTION_STRING')
        self.engine = create_engine(connection_string, echo=echo)
        Base.metadata.create_all(bind=self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    #################################################################
    # Adding and Retrieving Zettel

    def _add_zettel(self, zettel: Zettel):
        zettel_model = ZettelModel(zettel.id,
                                   zettel.recto.id,
                                   zettel.verso.id)
        self.session.add(zettel_model)
        self.session.commit()
    
    def add_zettel_list(self, zettel_list: list[Zettel]):
        counter = 0
        for zettel in zettel_list:
            zettel_model = ZettelModel(zettel)
            self.session.add(zettel_model)

            counter += 1
            if counter % 10000 == 0:
                self.session.commit()
                print(counter)

        else:
            self.session.commit()
            print(counter)

    def get_zettel(self):
        return self.session.query(ZettelModel).all()


    #################################################################
    # Adding and Retrieving Scans

    def _add_scan(self, scan: Scan):
        scan_model = ScanModel(scan)
        self.session.add(scan_model)
        self.session.commit()

    def add_scan_list(self, scans: list[Scan]):
        counter = 0
        for scan in scans:
            scan_model = ScanModel(scan)
            self.session.add(scan_model)

            counter += 1
            if counter % 10000 == 0:
                self.session.commit()
                print(counter)

        else:
            self.session.commit()
            print(counter)

    def add_path_list_as_scans(self, paths: list[str]):
        counter = 0
        for path in paths:
            scan_model = ScanModel(Scan(path))
            self.session.add(scan_model)

            counter += 1
            if counter % 10000 == 0:
                self.session.commit()
                print(counter)

        else:
            self.session.commit()
            print(counter)

    def get_scans(self):
        return self.session.query(ScanModel).all()


    #################################################################
    # Adding and Retrieving Landschaften

    def _add_landschaft(self,
                        abbreviation: str,
                        name: str,
                        description: str):
        landschaft_model = LandschaftModel(abbreviation,
                                           name,
                                           description)
        self.session.add(landschaft_model)
        self.session.commit()
    
    def add_landschaften(self, landschaften: list[tuple]):
        for landschaft in landschaften:
            landschaft_model = LandschaftModel(*landschaft)
            self.session.add(landschaft_model)
        self.session.commit()


    #################################################################
    # Adding and Retrieving Kreise

    def _add_kreis(self, abbreviation: str, name: str):
        kreis_model = KreisModel(abbreviation, name)
        self.session.add(kreis_model)
        self.session.commit()
    
    def add_kreise(self, kreise: list[tuple]):
        for kreis in kreise:
            kreis_model = KreisModel(*kreis)
            self.session.add(kreis_model)
        self.session.commit()

    def get_kreise(self):
        return self.session.query(KreisModel).all()


    #################################################################
    # Adding and Retrieving Orte

    def _add_ort(self, kreis: str, abbreviation: str, name: str):
        ort_model = OrtModel(kreis, abbreviation, name)
        self.session.add(ort_model)
        self.session.commit()
    
    def add_orte(self, orte: list[tuple]):
        for ort in orte:
            ort_model = OrtModel(*ort)
            self.session.add(ort_model)
        self.session.commit()

    def get_orte(self):
        return self.session.query(OrtModel).all()


    #################################################################
    # Adding and Retrieving Bounding Boxes

    def _add_boundingbox(self, dp: DataPoint):
        box_model = BoundingBoxModel(dp)
        self.session.add(box_model)
        self.session.commit()

    def add_boundingbox_probe(self, probe: Probe):
        counter = 0
        for dp in probe:
            box_model = BoundingBoxModel(dp)
            self.session.add(box_model)

            counter += 1
            if counter % 10000 == 0:
                self.session.commit()
                print(counter)
        else:
            self.session.commit()
            print(counter)

    def get_boundingboxes(self):
        return self.session.query(BoundingBoxModel).all()


    #################################################################
    # Adding and Retrieving Bounding Boxes

    def _add_ocr_result(self, dp: DataPoint):
        ocr_result_model = OCRResultModel(dp)
        self.session.add(ocr_result_model)
        self.session.commit()

    def add_ocr_probe(self, probe: Probe):
        counter = 0
        for dp in probe:
            ocr_result_model = OCRResultModel(dp)
            self.session.add(ocr_result_model)

            counter += 1
            if counter % 10000 == 0:
                self.session.commit()
                print(counter)
        else:
            self.session.commit()
            print(counter)

    def get_ocr_results(self):
        return self.session.query(OCRResultModel).all()


    #################################################################
    # Quieries
    #################################################################

    def quiery(self, stmt):
        return self.session.execue(stmt).scalaers().all()

    def get_missing_ocrs(self):
        stmt = (
            select(ScanModel.full_path)
            .where(
                ~exists().where(OCRResultModel.scan_id
                                == ScanModel.id)
            )
            .where(
                ScanModel.id.endswith("_1")
            )
        )
        return self.session.execute(stmt).scalars().all()
    
    def get_full_path(self, scan_id):
        stmt = (
            select(
                ScanModel.full_path
            )
            .where(
                ScanModel.id == scan_id
            )
        )
        return self.session.execute(stmt).scalars().all()
    
    def get_ocr_concat(self):
        stmt = (
            select(
                OCRResultModel.scan_id,
                func.group_concat(OCRResultModel.text, " | ").label("combined_text")
            )
            .group_by(OCRResultModel.scan_id)
        )
        return self.session.execute(stmt).all()

    def get_ocr_line_by_line(self):
        stmt = (
            select(
                func.group_concat(OCRResultModel.text, "Æ").label("combined_text")
            )
            .group_by(OCRResultModel.scan_id)
        )
        return self.session.execute(stmt).all()
    