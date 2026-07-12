import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CONDITIONS_FILE = (
    BASE_DIR
    / "datasets"
    / "conditions"
    / "conditions.csv"
)


def get_all_conditions():

    df = pd.read_csv(CONDITIONS_FILE)

    df = df.fillna("")

    return df.to_dict(orient="records")