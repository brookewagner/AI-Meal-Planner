
from src.recipe_search import load_recipes


def add_meal(meal_plan, day, recipe_id):
    """Add or replace a recipe for a specific day."""

    meal_plan[day] = recipe_id

    return meal_plan


def remove_meal(meal_plan, day):
    """Remove a recipe from a specific day."""

    if day in meal_plan:
        del meal_plan[day]

    return meal_plan


def generate_grocery_list(meal_plan, pantry):
    """Find ingredients missing from planned recipes."""

    recipes = load_recipes()

    recipe_lookup = {
        recipe["id"]: recipe
        for recipe in recipes
    }

    pantry_set = {
        item.strip().lower()
        for item in pantry
        if item.strip()
    }

    missing_ingredients = set()

    for recipe_id in meal_plan.values():

        recipe = recipe_lookup.get(recipe_id)

        if recipe is None:
            continue

        for ingredient in recipe["ingredients"]:

            ingredient = ingredient.strip().lower()

            if ingredient not in pantry_set:
                missing_ingredients.add(ingredient)

    return sorted(missing_ingredients)
