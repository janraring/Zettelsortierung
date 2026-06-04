import pandas as pd
import regex as re

regions = pd.read_csv("data/processed/Landschaften.csv", sep="\t")
region_tuples = list(
    zip(
        regions["Abkuerzung"].str.strip(),
        regions["Name"].str.strip(),
        regions["Beschreibung"].str.strip(),
    )
)

categories = ""
for abk, name, beschr in region_tuples:
    category = f"""ANON_{abk.upper()} = Sammlung(
        trace="{abk}|{name}",
        groups="Wortschatz|Anonym|{re.sub(" ", "", name)}",
        description="{beschr}",
        landschaft="{abk}",
    )
    """
    categories += category
print(categories)

with open("data/interim/classes_xy.txt", "w") as f:
    f.write(categories)
