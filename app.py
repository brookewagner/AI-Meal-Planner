
import streamlit as st

from src.recipe_search import search_recipes, load_recipes
from src.meal_planner import (
    add_meal,
    remove_meal,
    generate_grocery_list
)


st.set_page_config(
    page_title="AI Meal Planner",
    page_icon="🍽️",
    layout="centered"
)

# Session data
if "meal_plan" not in st.session_state:
    st.session_state.meal_plan = {}

if "pantry" not in st.session_state:
    st.session_state.pantry = []

if "recommendations" not in st.session_state:
    st.session_state.recommendations = []


st.title("🍽️ AI Meal Planner")
st.write("Find meals using ingredients you already have!")

# Pantry input
pantry_input = st.text_area(
    "What's in your pantry?",
    placeholder="eggs, cheese, spinach, rice"
)

# Dietary preference
diet = st.selectbox(
    "Dietary Preference",
    ["any", "vegetarian", "vegan"]
)

# Cooking time
max_time = st.slider(
    "Maximum Cooking Time (minutes)",
    min_value=5,
    max_value=120,
    value=30,
    step=5
)

# Find recipes
if st.button("Find Recipes", type="primary"):

    pantry = [
        item.strip().lower()
        for item in pantry_input.split(",")
        if item.strip()
    ]

    st.session_state.pantry = pantry

    if not pantry:
        st.session_state.recommendations = []
        st.warning("Please enter at least one ingredient.")
    else:
        st.session_state.recommendations = search_recipes(
            pantry,
            diet=diet,
            max_time=max_time
        )

# Display recommendations
recommendations = st.session_state.recommendations

if recommendations:

    st.subheader("Recommended Recipes")

    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    for recipe in recommendations[:5]:

        with st.container(border=True):
            st.subheader(recipe["name"])

            st.progress(recipe["score"])

            st.write(
                f"**Ingredient Match:** {recipe['score']:.0%}"
            )

            st.write(
                f"**Cooking Time:** {recipe['cook_time']} minutes"
            )

            st.write(
                "**Ingredients You Have:** "
                + ", ".join(recipe["available"])
            )

            st.write(
                "**Missing Ingredients:** "
                + (
                    ", ".join(recipe["missing"])
                    if recipe["missing"]
                    else "None!"
                )
            )

            # Select meal day
            day = st.selectbox(
                "Add to which day?",
                days,
                key=f"day_{recipe['id']}"
            )

            # Add selected meal
            if st.button(
                "Add to Meal Plan",
                key=f"add_{recipe['id']}"
            ):
                add_meal(
                    st.session_state.meal_plan,
                    day,
                    recipe["id"]
                )

                st.success(
                    f"{recipe['name']} added to {day}!"
                )

elif st.session_state.pantry:
    st.info("No matching recipes found.")


# Weekly meal plan
st.divider()
st.header("📅 My Weekly Meal Plan")

recipes = load_recipes()

recipe_lookup = {
    recipe["id"]: recipe
    for recipe in recipes
}

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

if not st.session_state.meal_plan:
    st.info("Your meal plan is empty.")

else:
    for day in days:

        if day not in st.session_state.meal_plan:
            continue

        recipe_id = st.session_state.meal_plan[day]
        recipe = recipe_lookup.get(recipe_id)

        if recipe is None:
            continue

        col1, col2 = st.columns([3, 1])

        with col1:
            st.write(f"**{day}:** {recipe['name']}")

        with col2:
            if st.button(
                "Remove",
                key=f"remove_{day}"
            ):
                remove_meal(
                    st.session_state.meal_plan,
                    day
                )
                st.rerun()


# Grocery list
st.divider()
st.header("🛒 Grocery List")

grocery_list = generate_grocery_list(
    st.session_state.meal_plan,
    st.session_state.pantry
)

if not st.session_state.meal_plan:
    st.info("Add meals to generate a grocery list.")

elif not grocery_list:
    st.success("You already have all the listed ingredients!")

else:
    st.write("Ingredients you need to buy:")

    for ingredient in grocery_list:
        st.checkbox(
            ingredient.capitalize(),
            key=f"grocery_{ingredient}"
        )


st.caption(
    "Prototype: Uses sample recipes and rule-based matching. "
    "Allergy safety is not yet validated."
)
