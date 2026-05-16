import regex as re
import pandas as pd

regions = pd.read_csv("data/processed/Orte.csv", sep="\t")
region_tuples = list(
    zip(regions["Kreis"].str.strip(), regions["Abkuerzung"].str.strip())
)

categories = ""
for kreis in regions["Kreis"].unique():
    category = f"""ANON_{kreis.upper()}_XY = Sammlung(
        trace="{kreis.title()} Xy",
        groups="Wortschatz|Anonym|{kreis.title()} Xy",
        kreis="{kreis.title()}",
        ort="Xy",
    )
    """
    categories += category
print(categories)

with open("data/interim/classes_xy.txt", "w") as f:
    f.write(categories)
