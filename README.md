# AI Meal Planner

**Team:** Colorado School of Meals

**Members:** Mitchell Chase, Cade Shiveley, Nicolas Finocchio, Rick Hank, Brooke Wagner

## Project Overview

AI Meal Planner is an application that helps users plan meals across multiple days, find recipes using ingredients they already have, and generate shopping lists for missing ingredients.

The application uses a large language model (LLM) to interpret user requests and recommend recipes based on available ingredients, dietary restrictions, allergies, and cooking preferences.

## Setup Instructions

**Project status:** In development. Final installation instructions will be added once the application is implemented.

Planned setup:

1. Clone the GitHub repository.
2. Install Python and the project dependencies.
3. Copy `.env.example` into a local `.env` file.
4. Add the provided OpenAI API key to the local `.env` file.
5. Follow the application startup instructions once implemented.

Never commit actual API keys or `.env` files.

## How to Run the Application

The application has not yet been implemented. Planned functionality includes:

1. Enter ingredients in the user's pantry.
2. Specify dietary preferences, allergies, and cooking time.
3. Receive recipe recommendations from the recipe database.
4. Add or remove meals from a multi-day meal plan.
5. Generate a shopping list for missing ingredients.

The actual run command will be documented when available.

## Evaluation and Reproducibility

We will evaluate the application using 10 test cases covering:

- Empty pantry
- Single ingredient
- Eggs and cheese recipes
- Vegetarian meals
- High-protein meals
- Balanced meals
- Seven-day meal preparation
- Missing ingredients
- Quick and easy meals
- Vegan meals

**Metric:** Percentage of test cases that satisfy the expected requirements.

**Success target:** At least 9 out of 10 test cases passing.

**Baseline:** A basic LLM prompt or Google search using the same user inputs.

The test dataset, evaluation scripts, and instructions for reproducing the results will be added during development.

## Models and Providers

**Provider:** OpenAI

**Planned models:**
- `gpt-6-luna` — request interpretation and meal selection
- `text-embedding-3-small` — recipe embeddings for similarity-based retrieval
- `omni-moderation-latest` — input moderation

**Other technologies:**
- Python
- Pydantic for structured outputs and validation
- Public recipe database (Food.com or TheMealDB)

## Application Architecture

The application will follow a fixed workflow:

1. User enters a meal-planning request.
2. Input moderation screens the request.
3. The LLM extracts user preferences and restrictions into structured fields.
4. The recipe database is filtered and searched.
5. The LLM selects and explains suitable recipes.
6. Python validation checks dietary restrictions and allergens.
7. Approved recipes are presented to the user.
8. Users can add recipes to a meal plan and create a shopping list.

## Usage and Cost Summary

The application will primarily use text-based API requests. Recipe embeddings will be generated once and cached to reduce repeated costs.

We expect relatively low usage and costs during testing because no image generation is required.

Actual API call counts, token usage, and costs will be recorded during development and evaluation.

## Data and Responsible AI

- Only public or synthetic data will be used during development and testing.
- Real user information will not be sent to model APIs during evaluation.
- Dietary restrictions and allergens will be checked through Python validation.
- The model will select recipes from an existing database instead of inventing recipes.
- API keys will be stored locally and excluded from GitHub.
- Meal recommendations will not be presented as professional nutritional or medical advice.

## AI-Use Disclosure

Generative AI was used to assist with drafting and organizing project documentation. The team will document any additional AI use for code generation, debugging, testing, and implementation.

All AI-assisted outputs will be reviewed and validated by team members.

## Project Status

Proposal stage. Implementation and evaluation are upcoming.
