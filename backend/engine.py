"""
CraveWise AI — Decision Engine

This is a transparent, rule-based scoring engine that mirrors the pipeline
described in the product doc:

    Health -> Goal -> Budget -> Pantry -> Time -> Nutrition -> Craving -> Decision

It does NOT require any paid API key, so the app is fully runnable today.
Where a real LLM call (Gemini) would add value — turning the scores into a
natural-language explanation, or handling messier free-text cravings — the
hook is marked clearly below (`explain_with_llm`) so you can wire in your own
Gemini/OpenAI key later without changing anything else.
"""
from services.spoonacular import get_recipe_media
from typing import List, Dict, Any
from data import get_all_recipes, HEALTHY_SWAPS
from services.spoonacular import search_recipes
from services.spoonacular import spoonacular_to_cravewise
from services.health_service import get_all_conditions
def _craving_score(recipe: Dict[str, Any], craving_text: str) -> int:
    craving_text = craving_text.lower().strip()
    if not craving_text:
        return 50
    score = 0
    if craving_text in recipe["name"].lower():
        score += 60
    if craving_text in recipe["base_dish"].lower():
        score += 40
    # loose keyword overlap as a fallback
    overlap = len(set(craving_text.split()) & set(recipe["base_dish"].split()))
    score += overlap * 15
    return min(score, 100)


def _health_score(recipe, conditions, goal):

    score = 60

    recipe_text = (
        recipe["name"]
        +
        " "
        +
        " ".join(recipe["ingredients"])
    ).lower()


    for condition in conditions:

        condition = condition.lower()


        for c in get_all_conditions():

            if c["name"].lower()==condition:


                recommended = c["recommended_foods"].lower()

                avoid = c["avoid_foods"].lower()


                for food in recommended.split(","):

                    if food.strip() in recipe_text:
                        score += 5


                for food in avoid.split(","):

                    if food.strip() in recipe_text:
                        score -= 10



    if goal=="weight_loss":

        if recipe["calories"] < 400:
            score +=10


    if recipe["protein"] >=20:
        score+=5


    return max(0,min(score,100))


def _pantry_match(recipe: Dict[str, Any], pantry: List[str]):
    pantry = {p.lower().strip() for p in pantry}
    have = [ing for ing in recipe["ingredients"] if ing.lower() in pantry]
    missing = [ing for ing in recipe["ingredients"] if ing.lower() not in pantry]
    match_pct = int(100 * len(have) / len(recipe["ingredients"])) if recipe["ingredients"] else 0
    return match_pct, missing


def _budget_time_fit(recipe: Dict[str, Any], budget: int, time_limit: int):
    budget_ok = budget is None or recipe["cost"] <= budget
    time_ok = time_limit is None or recipe["time_minutes"] <= time_limit
    return budget_ok, time_ok


def _build_explanation(recipe, conditions, goal, craving_text, budget, time_limit, missing):
    reasons = []
    if craving_text:
        reasons.append(f"you were craving \"{craving_text}\"")
    for c in conditions:
        cl = c.lower()
        if cl in ("diabetes", "diabetic") and "diabetic_friendly" in recipe["diet_tags"]:
            reasons.append("it's suitable for diabetes management")
        if cl == "pcos" and "pcos_friendly" in recipe["diet_tags"]:
            reasons.append("it's a good fit for PCOS")
    if goal == "weight_loss" and recipe["calories"] <= 350:
        reasons.append(f"it's only {recipe['calories']} kcal, supporting your weight-loss goal")
    if budget and recipe["cost"] <= budget:
        reasons.append(f"it fits your ₹{budget} budget (₹{recipe['cost']})")
    if time_limit and recipe["time_minutes"] <= time_limit:
        reasons.append(f"it's ready in {recipe['time_minutes']} minutes")
    if not missing:
        reasons.append("you already have every ingredient in your pantry")
    elif len(missing) <= 2:
        reasons.append(f"you're only missing {', '.join(missing)}")

    if not reasons:
        return f"{recipe['name']} is a solid all-round option based on your profile."
    return "Because " + "; ".join(reasons) + f", we recommend **{recipe['name']}**."


def explain_with_llm(prompt: str) -> str:
    """
    Placeholder hook for a real Gemini call.

    Example (once you have a GEMINI_API_KEY set as an env var):

        import google.generativeai as genai
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        model = genai.GenerativeModel("gemini-1.5-flash")
        return model.generate_content(prompt).text

    Left unimplemented here so the app runs with zero paid keys out of the box.
    """
    raise NotImplementedError("Wire up your Gemini API key here to replace rule-based text.")


def recommend(profile: Dict[str, Any], craving: str, pantry: List[str],
              budget: int = None, time_limit: int = None, top_n: int = 5):
    selected_conditions = profile.get("health_conditions", [])
    print("Selected Conditions:", selected_conditions)
    condition_database = get_all_conditions()

    condition_info = []

    for cond in condition_database:

        if cond["name"] in selected_conditions:

            condition_info.append(cond)
    goal = profile.get("goal", "maintenance")

    scored = []
    recipes = search_recipes(craving, number=10)
    print("Recipes from Spoonacular:", len(recipes))

    for r in recipes[:5]:
        print(r["name"] if "name" in r else r.get("title"))
        if recipes:
    
            recipes = [spoonacular_to_cravewise(r) for r in recipes]
    
        else:
        
            recipes = get_all_recipes()
    
    for recipe in recipes:
        health = _health_score(recipe, selected_conditions, goal)
        print(recipe["name"], "Health Score:", health)
        crave = _craving_score(recipe, craving)
        pantry_pct, missing = _pantry_match(recipe, pantry)
        budget_ok, time_ok = _budget_time_fit(recipe, budget, time_limit)

        total = round(health * 0.35 + crave * 0.35 + pantry_pct * 0.20 +
                       (10 if budget_ok else 0) + (10 if time_ok else -10), 1)
        tags = []

        if recipe.get("protein", 0) >= 20:
            tags.append("High Protein")

        if recipe.get("fiber", 0) >= 5:
            tags.append("High Fiber")

        if recipe.get("calories", 9999) <= 450:
            tags.append("Low Calorie")

        if recipe.get("time_minutes", 999) <= 30:
            tags.append("Quick Meal")

        if budget and recipe.get("cost", 0) <= budget:
            tags.append("Budget Friendly")

        conditions_lower = [c.lower() for c in selected_conditions]

        if "diabetes" in conditions_lower:
            tags.append("Diabetes Friendly")

        if "pcos" in conditions_lower:
            tags.append("PCOS Friendly")
        swaps = {ing: HEALTHY_SWAPS[ing] for ing in recipe["ingredients"] if ing in HEALTHY_SWAPS}
        media = get_recipe_media(recipe["name"])
        scored.append({
            **recipe,
            "health_score": health,
            "craving_score": crave,
            "pantry_match_pct": pantry_pct,
            "missing_ingredients": missing,
            "budget_ok": budget_ok,
            "time_ok": time_ok,
            "total_score": total,
            "ai_match": min(100, int(total)),
            "tags": tags,
            "explanation": _build_explanation(recipe, selected_conditions, goal, craving, budget, time_limit, missing),
            "healthy_swaps": swaps,
            "image": media["image"],
            "youtube": media["youtube"],

        })

    scored.sort(key=lambda r: r["total_score"], reverse=True)
    return scored[:top_n]
