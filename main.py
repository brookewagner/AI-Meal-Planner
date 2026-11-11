
# Main function for our application 

from src.recipe_search import search_recipes


def main():
    print("Welcome to AI Meal Planner!")

    pantry_input = input(
        "Enter your ingredients (separated by commas): "
    )

    ingredients = [
        item.strip().lower()
        for item in pantry_input.split(",")
        if item.strip()
    ]

    print("\nYour pantry contains:")

    for ingredient in ingredients:
        print(f"- {ingredient}")

    
    # Ask for dietary preferences
    diet = input(
        "\nDiet (any, vegetarian, vegan): "
    ).strip().lower()

    if diet not in ["any", "vegetarian", "vegan"]:
        print("Invalid diet. Using 'any'.")
        diet = "any"

    # Ask for maximum cooking time
    time_input = input(
        "Maximum cooking time in minutes (Enter to skip): "
    ).strip()

    if time_input:
        try:
            max_time = int(time_input)
            if max_time <= 0:
                print("Time must be positive. Skipping time filter.")
                max_time = None
        except ValueError:
            print("Invalid time. Skipping time filter.")
            max_time = None
    else:
        max_time = None

    # Search using pantry and preferences
    recommendations = search_recipes(
        ingredients,
        diet=diet,
        max_time=max_time
    )


    if not recommendations:
        print("\nNo matching recipes found.")
        return

    print("\nRecommended Recipes:\n")

    for recipe in recommendations[:5]:
        print(f"Recipe: {recipe['name']}")
        print(f"Match: {recipe['score']:.0%}")
        print(f"Have: {', '.join(recipe['available'])}")
        print(f"Missing: {', '.join(recipe['missing'])}")
        print(f"Cook time: {recipe['cook_time']} minutes")
        print("-" * 30)


if __name__ == "__main__":
    main()

