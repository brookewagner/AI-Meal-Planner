
import streamlit as st
from src.recipe_search import search_recipes

st.set_page_config(
    page_title="AI Meal Planner",
    page_icon="🍽️",
    layout="centered"
)

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

# Maximum cooking time
max_time = st.slider(
    "Maximum Cooking Time (minutes)",
    min_value=5,
    max_value=120,
    value=30,
    step=5
)

# Recommendation button
if st.button("Find Recipes", type="primary"):

    pantry = [
        item.strip().lower()
        for item in pantry_input.split(",")
        if item.strip()
    ]

    if not pantry:
        st.warning("Please enter at least one ingredient.")
    else:
        recommendations = search_recipes(
            pantry,
            diet=diet,
            max_time=max_time
        )

        if not recommendations:
            st.info("No matching recipes found.")
        else:
            st.subheader("Recommended Recipes")

            for recipe in recommendations[:5]:
                with st.container(border=True):
                    st.subheader(recipe["name"])

                    st.progress(recipe["score"])
                    st.write(
                        f"**Ingredient Match:** "
                        f"{recipe['score']:.0%}"
                    )

                    st.write(
                        f"**Cooking Time:** "
                        f"{recipe['cook_time']} minutes"
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

st.caption(
    "Prototype: Uses sample recipes and rule-based "
    "matching. Allergy safety is not yet validated."
)