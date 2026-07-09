"""
Master Health Database

Every health condition supported by CraveWise
is defined here.

Future:
Database -> Supabase
Admin Panel -> Add new diseases without coding
"""

from .conditions import CONDITIONS
from .allergies import ALLERGIES
from .surgeries import SURGERIES
from .diets import DIETS
from .life_stages import LIFE_STAGES
import pandas as pd
from pathlib import Path



HEALTH_DATABASE = {
    "conditions": CONDITIONS,
    "allergies": ALLERGIES,
    "surgeries": SURGERIES,
    "diets": DIETS,
    "life_stages": LIFE_STAGES,
}

BASE_DIR = Path(__file__).resolve().parent.parent

ALLERGY_FILE = BASE_DIR / "datasets" / "allergies" / "allergies.csv"
def get_all_allergies():
    df = pd.read_csv(ALLERGY_FILE)
    return df.fillna("").to_dict(orient="records")