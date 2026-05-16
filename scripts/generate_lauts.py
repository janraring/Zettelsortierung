import regex as re
import pandas as pd

regions = pd.read_csv("data/processed/Orte.csv", sep="\t")
region_tuples = list(
    zip(regions["Kreis"].str.strip(), regions["Abkuerzung"].str.strip())
)

categories = ""
for rt in region_tuples:
    kreis, ort = rt
    category = f"""LAUT_{kreis.upper()}_{ort.upper()} = Sammlung(
        trace="{kreis.title()} {ort.title()}",
        groups="Lautschrift|{kreis.title()} {ort.title()}",
        kreis="{kreis.title()}",
        ort="{ort.title()}",
    )
    """
    categories += category

with open("data/interim/classes_laut.txt", "w") as f:
    f.write(categories)
