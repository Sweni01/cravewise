def spoonacular_to_cravewise(recipe):

    nutrients = {}

    nutrition = recipe.get("nutrition", {}).get("nutrients", [])

    for n in nutrition:
        nutrients[n["name"]] = n["amount"]

    return {

        "id": recipe.get("id"),

        "name": recipe.get("title"),

        "image": recipe.get("image"),

        "base_dish": recipe.get("title"),

        "ingredients": [],

        "diet_tags": [],

        "calories": nutrients.get("Calories", 0),

        "protein": nutrients.get("Protein", 0),

        "carbs": nutrients.get("Carbohydrates", 0),

        "fat": nutrients.get("Fat", 0),

        "fiber": nutrients.get("Fiber", 0),

        "time_minutes": recipe.get("readyInMinutes", 30),

        "difficulty": "Medium",

        "cost": 250

    }
