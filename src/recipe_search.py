
import json
from pathlib import Path


# Find the recipes.json file
DATA_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "recipes.json"
)


def load_recipes():
    """Load recipes from our JSON database."""

    with open(DATA_PATH, "r", encoding="utf-8") as file:
        recipes = json.load(file)

    return recipes


def search_recipes(pantry, diet="any", max_time=None):
    """Find recipes that match the user's ingredients."""

    recipes = load_recipes()

    # Convert pantry ingredients to lowercase
    pantry_set = {
        ingredient.strip().lower()
        for ingredient in pantry
        if ingredient.strip()
    }

    if not pantry_set:
        return []

    results = []

    for recipe in recipes:

        # Filter recipes by dietary preference
        if diet == "vegan" and recipe["diet"] != "vegan":
            continue

        if diet == "vegetarian" and recipe["diet"] not in [
            "vegetarian", "vegan"
        ]:
            continue

        # Filter recipes by maximum cooking time
        if max_time is not None:
            if recipe["cook_time"] > max_time:
                continue

        # Ingredients required by this recipe
        required = {
            ingredient.lower()
            for ingredient in recipe["ingredients"]
        }

        # Ingredients the user already has
        available = sorted(required & pantry_set)

        # Ingredients the user still needs
        missing = sorted(required - pantry_set)

        # Calculate ingredient match percentage
        match_score = len(available) / len(required)

        # Only recommend recipes with at least one match
        if available:
            results.append({
                "id": recipe["id"],
                "name": recipe["name"],
                "score": match_score,
                "available": available,
                "missing": missing,
                "cook_time": recipe["cook_time"]
            })

    # Sort recommendations by highest match percentage
    results.sort(
        key=lambda recipe: (
            -recipe["score"],
            len(recipe["missing"]),
            recipe["cook_time"]
        )
    )

    return results
