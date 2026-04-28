import pytest
import pandas as pd

from zettelsortierung.Sammlungen import Sammlungen


def test_sammlung():
    regions = pd.read_csv("data/processed/Orte.csv", sep="\t")
    region_tuples = list(
        zip(regions["Kreis"].str.strip(), regions["Abkuerzung"].str.strip())
    )

    for sammlung in Sammlungen:
        if (kreis := sammlung.value.kreis) is not None:
            assert kreis in regions["Kreis"].values, f"Kreis {kreis} ist nicht bekannt."
        if (abk := sammlung.value.ort) is not None:
            assert abk in regions["Abkuerzung"].values, f"Ort {abk} ist nicht bekannt."
            assert kreis is not None, f"Ort {abk} ist keinem Kreis zugeordnet."
            assert (
                kreis,
                abk,
            ) in region_tuples, f"Die Kombination ({kreis}, {abk}) ist nicht bekannt."
