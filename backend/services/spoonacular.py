import os
import json
import requests
from pathlib import Path
from dotenv import load_dotenv
from services.youtube import get_video

load_dotenv()

API_KEY = os.getenv("SPOONACULAR_API_KEY")

BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"
INFO_URL = "https://api.spoonacular.com/recipes/{id}/information"

CACHE_FILE = (
    Path(__file__).resolve().parent.parent
    / "cache"
    / "recipe_media.json"
)
def load_cache():

    if not CACHE_FILE.exists():

        return {}

    with open(CACHE_FILE, "r", encoding="utf-8") as f:

        return json.load(f)


def save_cache(cache):

    with open(CACHE_FILE, "w", encoding="utf-8") as f:

        json.dump(cache, f, indent=4)
def get_recipe_media(recipe_name: str):

    cache = load_cache()

    key = recipe_name.lower().strip()

    if key in cache:

        return cache[key]

    try:

        response = requests.get(

            BASE_URL,

            params={

                "query": recipe_name,

                "number": 1,

                "apiKey": API_KEY

            },

            timeout=10

        )

        data = response.json()

        if data.get("results"):

            recipe = data["results"][0]

            media = {

                "image": recipe.get("image"),

                "youtube": get_video(recipe_name)
            }

        else:

            media = {

                "image": None,

                "youtube": get_video(recipe_name)

            }

    except Exception:

        media = {

            "image": None,

            
            "youtube": get_video(recipe_name)
        }

    cache[key] = media

    save_cache(cache)

    return media

def search_recipes(query: str, number: int = 20):

    try:

        response = requests.get(
            BASE_URL,
            params={
                "query": query,
                "number": number,
                "apiKey": API_KEY
            },
            timeout=15
        )

        recipes = response.json().get("results", [])

        full_recipes = []

        for recipe in recipes:

            info = requests.get(
                INFO_URL.format(id=recipe["id"]),
                params={
                    "includeNutrition": True,
                    "apiKey": API_KEY
                }
            )

            if info.status_code == 200:
                full_recipes.append(info.json())

        return full_recipes

    except Exception as e:

        print(e)

        return []

def spoonacular_to_cravewise(recipe):

    nutrients = {}

    for nutrient in recipe.get("nutrition", {}).get("nutrients", []):
        nutrients[nutrient["name"]] = nutrient["amount"]

    ingredients = []

    for ingredient in recipe.get("extendedIngredients", []):
        ingredients.append(ingredient["name"])

    return {

        "id": str(recipe.get("id")),

        "name": recipe.get("title", ""),

        "base_dish": recipe.get("title", "").lower(),

        "ingredients": ingredients,

        "calories": nutrients.get("Calories", 0),

        "protein": nutrients.get("Protein", 0),

        "carbs": nutrients.get("Carbohydrates", 0),

        "fat": nutrients.get("Fat", 0),

        "fiber": nutrients.get("Fiber", 0),

        "cost": recipe.get("pricePerServing", 200) / 100,

        "time_minutes": recipe.get("readyInMinutes", 30),

        "difficulty": "Easy",

        "diet_tags": recipe.get("diets", []),

        "video_query": recipe.get("title", "")
    }    