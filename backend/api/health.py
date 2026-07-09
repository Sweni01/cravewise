from fastapi import APIRouter

from services.health_service import get_all_conditions
from health.database import get_all_allergies
router = APIRouter()

@router.get("/allergies")
def get_allergy_list():
    return get_all_allergies()
@router.get("/conditions")

def conditions():

    return get_all_conditions()