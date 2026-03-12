from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True, slots=True)
class Label:
    sammlung: Enum
    confidence: float


@dataclass(frozen=True, slots=True)
class Classifier:
    title: str
    description: str


class Classifiers(Enum):
    MANUELL = Classifier("Manuell", "Händisch gelabelt")
    OCR = Classifier("OCR", "Mittels OCR-Ergebnissen sortiert")


@dataclass(frozen=True, slots=True)
class Sammlung:
    title: str
    description: str
    search_term: str | None = None
    landschaft: str | None = None
    kreis: str | None = None
    ort: str | None = None


class Sammlungen(Enum):
    SKIPPED = Sammlung(title="Skipped", description="Vorerst übersprungene Zettel")
    FRAGEBOGEN = Sammlung(
        title="Fragebogen",
        description="Verzettelung eines nicht weiter bestimmten Fragebogens",
    )
    ECKARDT = Sammlung(
        title="Eckard",
        description="Schlachthofdirektor Dr. Eckardt (Wellinghofen b. Dortmund)",
        kreis="Dor",
        ort="Wl",
    )
