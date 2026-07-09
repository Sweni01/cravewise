from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from api.health import router as health_router
from engine import recommend
from data import get_all_recipes

app = FastAPI(title="CraveWise AI API")

app.include_router(
    health_router,
    prefix="/api/health",
    tags=["Health"]
)


# Allow the simple frontend (opened as a local file or served separately) to call this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Profile(BaseModel):
    age: Optional[int] = None
    gender: Optional[str] = None
    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None
    activity_level: Optional[str] = "moderate"
    health_conditions: List[str] = []
    allergies: List[str] = []
    goal: Optional[str] = "maintenance"  # weight_loss | muscle_gain | maintenance
    cuisine_preference: Optional[str] = None


class RecommendRequest(BaseModel):
    profile: Profile
    craving: str = ""
    pantry: List[str] = []
    budget: Optional[int] = None
    time_limit_minutes: Optional[int] = None


@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "CraveWise AI"}


@app.get("/api/recipes")
def list_recipes():
    """Module 2/3 support: browse the full recipe catalog."""
    return get_all_recipes()


@app.post("/api/recommend")
def get_recommendation(req: RecommendRequest):
    """
    Core Module 4 endpoint: the AI Decision Engine.
    Returns ranked recipes with health/craving scores, pantry match,
    a plain-English explanation, and healthy ingredient swaps.
    """
    results = recommend(
        profile=req.profile.dict(),
        craving=req.craving,
        pantry=req.pantry,
        budget=req.budget,
        time_limit=req.time_limit_minutes,
    )
    return {"count": len(results), "recommendations": results}
