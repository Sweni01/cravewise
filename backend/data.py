"""
CraveWise AI — sample recipe dataset.

In a production version, this would be replaced/augmented by a live call to
Spoonacular (recipes) + USDA FoodData Central (nutrition). The shape of each
recipe dict below intentionally matches what those APIs would give you, so
swapping in real data later only means editing `get_all_recipes()`.
"""

RECIPES = [
    {
        "id": "r1",
        "name": "Whole Wheat Paneer Pizza",
        "base_dish": "pizza",
        "ingredients": ["whole wheat flour", "paneer", "tomato", "onion", "cheese", "bell pepper"],
        "calories": 420, "protein": 24, "carbs": 45, "fat": 14, "fiber": 6,
        "cost": 180, "time_minutes": 25, "difficulty": "Easy",
        "diet_tags": ["diabetic_friendly", "pcos_friendly", "vegetarian", "high_protein"],
        "video_query": "healthy whole wheat paneer pizza recipe",
    },
    {
        "id": "r2",
        "name": "Cauliflower Crust Pizza",
        "base_dish": "pizza",
        "ingredients": ["cauliflower", "egg", "cheese", "tomato", "oregano"],
        "calories": 310, "protein": 20, "carbs": 18, "fat": 16, "fiber": 5,
        "cost": 240, "time_minutes": 40, "difficulty": "Medium",
        "diet_tags": ["low_carb", "diabetic_friendly", "pcos_friendly", "vegetarian"],
        "video_query": "low carb cauliflower crust pizza recipe",
    },
    {
        "id": "r3",
        "name": "Grilled Paneer Wrap",
        "base_dish": "pizza",  # cross-craving alternative
        "ingredients": ["whole wheat tortilla", "paneer", "onion", "yogurt", "lettuce"],
        "calories": 350, "protein": 22, "carbs": 30, "fat": 12, "fiber": 4,
        "cost": 120, "time_minutes": 15, "difficulty": "Easy",
        "diet_tags": ["pcos_friendly", "vegetarian", "high_protein"],
        "video_query": "healthy paneer wrap recipe",
    },
    {
        "id": "r4",
        "name": "Butter Chicken (Lighter Version)",
        "base_dish": "butter chicken",
        "ingredients": ["chicken", "yogurt", "onion", "tomato", "cashew", "spices"],
        "calories": 480, "protein": 38, "carbs": 20, "fat": 22, "fiber": 3,
        "cost": 260, "time_minutes": 35, "difficulty": "Medium",
        "diet_tags": ["high_protein", "pcos_friendly"],
        "video_query": "healthy low fat butter chicken recipe",
    },
    {
        "id": "r5",
        "name": "Yogurt-Marinated Tandoori Chicken",
        "base_dish": "butter chicken",
        "ingredients": ["chicken", "yogurt", "onion", "tomato", "spices", "lemon"],
        "calories": 340, "protein": 42, "carbs": 8, "fat": 12, "fiber": 2,
        "cost": 220, "time_minutes": 25, "difficulty": "Easy",
        "diet_tags": ["low_carb", "diabetic_friendly", "pcos_friendly", "high_protein"],
        "video_query": "tandoori chicken healthy recipe",
    },
    {
        "id": "r6",
        "name": "Tomato Onion Chicken Curry (No Cream)",
        "base_dish": "butter chicken",
        "ingredients": ["chicken", "tomato", "onion", "yogurt", "spices"],
        "calories": 300, "protein": 36, "carbs": 12, "fat": 9, "fiber": 3,
        "cost": 200, "time_minutes": 30, "difficulty": "Easy",
        "diet_tags": ["diabetic_friendly", "pcos_friendly", "low_carb", "high_protein"],
        "video_query": "no cream chicken curry recipe healthy",
    },
    {
        "id": "r7",
        "name": "Vegetable Oats Upma",
        "base_dish": "upma",
        "ingredients": ["oats", "onion", "tomato", "carrot", "peas", "mustard seeds"],
        "calories": 220, "protein": 8, "carbs": 32, "fat": 6, "fiber": 7,
        "cost": 60, "time_minutes": 15, "difficulty": "Easy",
        "diet_tags": ["diabetic_friendly", "vegan", "vegetarian"],
        "video_query": "vegetable oats upma recipe",
    },
    {
        "id": "r8",
        "name": "Moong Dal Khichdi",
        "base_dish": "khichdi",
        "ingredients": ["rice", "moong dal", "onion", "tomato", "ghee", "cumin"],
        "calories": 280, "protein": 12, "carbs": 42, "fat": 6, "fiber": 6,
        "cost": 70, "time_minutes": 30, "difficulty": "Easy",
        "diet_tags": ["diabetic_friendly", "vegetarian", "pcos_friendly"],
        "video_query": "moong dal khichdi healthy recipe",
    },
    {
        "id": "r9",
        "name": "Greek Yogurt Chicken Salad",
        "base_dish": "salad",
        "ingredients": ["chicken", "yogurt", "lettuce", "cucumber", "tomato", "lemon"],
        "calories": 260, "protein": 34, "carbs": 10, "fat": 8, "fiber": 4,
        "cost": 180, "time_minutes": 15, "difficulty": "Easy",
        "diet_tags": ["low_carb", "diabetic_friendly", "pcos_friendly", "high_protein"],
        "video_query": "greek yogurt chicken salad recipe",
    },
    {
        "id": "r10",
        "name": "Paneer Bhurji Sandwich",
        "base_dish": "sandwich",
        "ingredients": ["bread", "paneer", "onion", "tomato", "capsicum"],
        "calories": 340, "protein": 20, "carbs": 34, "fat": 12, "fiber": 5,
        "cost": 90, "time_minutes": 15, "difficulty": "Easy",
        "diet_tags": ["vegetarian", "pcos_friendly"],
        "video_query": "paneer bhurji sandwich recipe",
    },
    {
        "id": "r11",
        "name": "Egg & Vegetable Stir Fry",
        "base_dish": "stir fry",
        "ingredients": ["egg", "onion", "bell pepper", "carrot", "soy sauce"],
        "calories": 300, "protein": 22, "carbs": 16, "fat": 15, "fiber": 4,
        "cost": 110, "time_minutes": 15, "difficulty": "Easy",
        "diet_tags": ["low_carb", "diabetic_friendly", "high_protein"],
        "video_query": "egg vegetable stir fry recipe",
    },
    {
        "id": "r12",
        "name": "Banana Oats Smoothie",
        "base_dish": "smoothie",
        "ingredients": ["banana", "oats", "milk", "peanut butter"],
        "calories": 310, "protein": 12, "carbs": 46, "fat": 9, "fiber": 6,
        "cost": 70, "time_minutes": 5, "difficulty": "Easy",
        "diet_tags": ["vegetarian"],
        "video_query": "banana oats smoothie recipe",
    },
]


def get_all_recipes():
    """Swap this for a live Spoonacular/USDA call in production."""
    return RECIPES


HEALTHY_SWAPS = {
    "white flour": "whole wheat flour",
    "maida": "whole wheat flour",
    "sugar": "dates or jaggery (in moderation)",
    "cream": "greek yogurt",
    "butter": "olive oil",
    "white rice": "brown rice or cauliflower rice",
    "refined oil": "olive oil or mustard oil",
    "condensed milk": "low-fat milk + a natural sweetener",
}
