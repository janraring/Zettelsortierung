from typing import Protocol


class Measurement(Protocol):
    ...


class FeatureExtractor(Protocol):
    def extract():
        ...