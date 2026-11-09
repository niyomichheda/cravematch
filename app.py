
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CraveMatch",
    page_icon="🍕",
    layout="wide"
)

st.title("🍽️ CraveMatch")
st.subheader("Find food that matches your cravings!")

st.write(
    "Tell us what you feel like eating, "
    "and we will find your perfect food match!"
)

# Sample food dataset
data = {
    "Dish": [
        "Paneer Tikka",
        "Veg Pizza",
        "Veg Biryani",
        "White Sauce Pasta",
        "Masala Dosa",
        "Veg Burger",
        "Hakka Noodles",
        "Falafel Wrap"
    ],
    "Cuisine": [
        "Indian", "Italian", "Indian", "Italian",
        "South Indian", "American", "Chinese", "Middle Eastern"
    ],
    "Diet": [
        "Vegetarian", "Vegetarian", "Vegetarian",
        "Vegetarian", "Vegetarian", "Vegetarian",
        "Vegetarian", "Vegetarian"
    ],
    "Price (AED)": [25, 35, 30, 32, 18, 28, 24, 22],
    "Rating": [4.7, 4.5, 4.8, 4.4, 4.6, 4.2, 4.3, 4.5],
    "Mood": [
        "Spicy", "Cheesy", "Spicy", "Creamy",
        "Comfort Food", "Comfort Food", "Spicy", "Light"
    ]
}

df = pd.DataFrame(data)

st.sidebar.header("❤️ Your Food Preferences")

cuisine = st.sidebar.selectbox(
    "Choose your cuisine",
    ["Any"] + sorted(df["Cuisine"].unique().tolist())
)

mood = st.sidebar.selectbox(
    "What are you craving?",
    ["Any"] + sorted(df["Mood"].unique().tolist())
)

budget = st.sidebar.slider(
    "Your maximum budget (AED)",
    min_value=10,
    max_value=100,
    value=40
)

min_rating = st.sidebar.slider(
    "Minimum food rating",
    min_value=1.0,
    max_value=5.0,
    value=4.0,
    step=0.1
)

# Match food preferences
results = df[
    (df["Price (AED)"] <= budget) &
    (df["Rating"] >= min_rating)
]

if cuisine != "Any":
    results = results[results["Cuisine"] == cuisine]

if mood != "Any":
    results = results[results["Mood"] == mood]

st.markdown("### ✨ Your Food Matches")

col1, col2, col3 = st.columns(3)

col1.metric("Total Dishes", len(df))
col2.metric("Matching Dishes", len(results))
col3.metric("Maximum Budget", f"AED {budget}")

if not results.empty:
    st.success(f"We found {len(results)} food matches for you!")

    for _, food in results.iterrows():
        with st.container(border=True):
            st.subheader("🍴 " + food["Dish"])
            st.write("Cuisine:", food["Cuisine"])
            st.write("Mood:", food["Mood"])
            st.write("Price:", f"AED {food['Price (AED)']}")
            st.write("Rating:", f"⭐ {food['Rating']}/5")
else:
    st.warning(
        "No exact matches found. Try changing your preferences!"
    )

st.markdown("---")
st.caption("CraveMatch | Your cravings, perfectly matched ❤️")
