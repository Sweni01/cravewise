from fastapi import APIRouter
from services.health_service import get_all_conditions

router = APIRouter()


@router.get("/conditions/grouped")
def grouped_conditions():

    conditions = get_all_conditions()

    groups = {}

    for c in conditions:
        category = c["category"]

        if category not in groups:
            groups[category] = []

        groups[category].append(c)

    return groups