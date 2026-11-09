
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
data = [
    # INDIAN
    {"Dish": "Paneer Tikka", "Cuisine": "Indian", "Diet": "Vegetarian", "Price (AED)": 30, "Rating": 4.7, "Mood": "Spicy"},
    {"Dish": "Veg Biryani", "Cuisine": "Indian", "Diet": "Vegetarian", "Price (AED)": 35, "Rating": 4.8, "Mood": "Spicy"},
    {"Dish": "Butter Paneer", "Cuisine": "Indian", "Diet": "Vegetarian", "Price (AED)": 40, "Rating": 4.6, "Mood": "Creamy"},
    {"Dish": "Chole Bhature", "Cuisine": "Indian", "Diet": "Vegetarian", "Price (AED)": 25, "Rating": 4.5, "Mood": "Comfort Food"},
    {"Dish": "Pav Bhaji", "Cuisine": "Indian", "Diet": "Vegetarian", "Price (AED)": 22, "Rating": 4.6, "Mood": "Spicy"},
    {"Dish": "Palak Paneer", "Cuisine": "Indian", "Diet": "Vegetarian", "Price (AED)": 35, "Rating": 4.4, "Mood": "Creamy"},
    {"Dish": "Dal Makhani", "Cuisine": "Indian", "Diet": "Vegetarian", "Price (AED)": 30, "Rating": 4.5, "Mood": "Comfort Food"},
    {"Dish": "Veg Kathi Roll", "Cuisine": "Indian", "Diet": "Vegetarian", "Price (AED)": 20, "Rating": 4.3, "Mood": "Spicy"},
    {"Dish": "Aloo Paratha", "Cuisine": "Indian", "Diet": "Vegetarian", "Price (AED)": 18, "Rating": 4.4, "Mood": "Comfort Food"},

    # ITALIAN
    {"Dish": "Veg Pizza", "Cuisine": "Italian", "Diet": "Vegetarian", "Price (AED)": 35, "Rating": 4.5, "Mood": "Cheesy"},
    {"Dish": "White Sauce Pasta", "Cuisine": "Italian", "Diet": "Vegetarian", "Price (AED)": 40, "Rating": 4.3, "Mood": "Creamy"},
    {"Dish": "Margherita Pizza", "Cuisine": "Italian", "Diet": "Vegetarian", "Price (AED)": 30, "Rating": 4.6, "Mood": "Cheesy"},
    {"Dish": "Pesto Pasta", "Cuisine": "Italian", "Diet": "Vegetarian", "Price (AED)": 45, "Rating": 4.7, "Mood": "Light"},
    {"Dish": "Garlic Bread", "Cuisine": "Italian", "Diet": "Vegetarian", "Price (AED)": 20, "Rating": 4.2, "Mood": "Comfort Food"},
    {"Dish": "Mac and Cheese", "Cuisine": "Italian", "Diet": "Vegetarian", "Price (AED)": 38, "Rating": 4.8, "Mood": "Cheesy"},
    {"Dish": "Arrabbiata Pasta", "Cuisine": "Italian", "Diet": "Vegetarian", "Price (AED)": 35, "Rating": 4.4, "Mood": "Spicy"},
    {"Dish": "Mushroom Risotto", "Cuisine": "Italian", "Diet": "Vegetarian", "Price (AED)": 48, "Rating": 4.6, "Mood": "Creamy"},
    {"Dish": "Veg Lasagna", "Cuisine": "Italian", "Diet": "Vegetarian", "Price (AED)": 45, "Rating": 4.5, "Mood": "Cheesy"},

    # SOUTH INDIAN
    {"Dish": "Masala Dosa", "Cuisine": "South Indian", "Diet": "Vegetarian", "Price (AED)": 20, "Rating": 4.6, "Mood": "Spicy"},
    {"Dish": "Idli Sambar", "Cuisine": "South Indian", "Diet": "Vegetarian", "Price (AED)": 15, "Rating": 4.3, "Mood": "Light"},
    {"Dish": "Medu Vada", "Cuisine": "South Indian", "Diet": "Vegetarian", "Price (AED)": 18, "Rating": 4.4, "Mood": "Comfort Food"},
    {"Dish": "Rava Dosa", "Cuisine": "South Indian", "Diet": "Vegetarian", "Price (AED)": 22, "Rating": 4.5, "Mood": "Light"},
    {"Dish": "Uttapam", "Cuisine": "South Indian", "Diet": "Vegetarian", "Price (AED)": 20, "Rating": 4.3, "Mood": "Comfort Food"},
    {"Dish": "Pongal", "Cuisine": "South Indian", "Diet": "Vegetarian", "Price (AED)": 18, "Rating": 4.2, "Mood": "Comfort Food"},
    {"Dish": "Curd Rice", "Cuisine": "South Indian", "Diet": "Vegetarian", "Price (AED)": 18, "Rating": 4.4, "Mood": "Light"},
    {"Dish": "Mysore Masala Dosa", "Cuisine": "South Indian", "Diet": "Vegetarian", "Price (AED)": 25, "Rating": 4.7, "Mood": "Spicy"},

    # AMERICAN
    {"Dish": "Veg Burger", "Cuisine": "American", "Diet": "Vegetarian", "Price (AED)": 35, "Rating": 4.3, "Mood": "Comfort Food"},
    {"Dish": "French Fries", "Cuisine": "American", "Diet": "Vegetarian", "Price (AED)": 15, "Rating": 4.2, "Mood": "Comfort Food"},
    {"Dish": "Cheese Sandwich", "Cuisine": "American", "Diet": "Vegetarian", "Price (AED)": 25, "Rating": 4.4, "Mood": "Cheesy"},
    {"Dish": "Veg Hot Dog", "Cuisine": "American", "Diet": "Vegetarian", "Price (AED)": 30, "Rating": 4.1, "Mood": "Comfort Food"},
    {"Dish": "Loaded Nachos", "Cuisine": "American", "Diet": "Vegetarian", "Price (AED)": 28, "Rating": 4.5, "Mood": "Cheesy"},
    {"Dish": "Onion Rings", "Cuisine": "American", "Diet": "Vegetarian", "Price (AED)": 18, "Rating": 4.2, "Mood": "Comfort Food"},
    {"Dish": "Veg Wrap", "Cuisine": "American", "Diet": "Vegetarian", "Price (AED)": 30, "Rating": 4.3, "Mood": "Light"},
    {"Dish": "Macaroni Salad", "Cuisine": "American", "Diet": "Vegetarian", "Price (AED)": 25, "Rating": 4.1, "Mood": "Creamy"},

    # CHINESE
    {"Dish": "Hakka Noodles", "Cuisine": "Chinese", "Diet": "Vegetarian", "Price (AED)": 28, "Rating": 4.5, "Mood": "Spicy"},
    {"Dish": "Veg Fried Rice", "Cuisine": "Chinese", "Diet": "Vegetarian", "Price (AED)": 25, "Rating": 4.3, "Mood": "Comfort Food"},
    {"Dish": "Spring Rolls", "Cuisine": "Chinese", "Diet": "Vegetarian", "Price (AED)": 20, "Rating": 4.4, "Mood": "Comfort Food"},
    {"Dish": "Chilli Paneer", "Cuisine": "Chinese", "Diet": "Vegetarian", "Price (AED)": 35, "Rating": 4.6, "Mood": "Spicy"},
    {"Dish": "Veg Manchurian", "Cuisine": "Chinese", "Diet": "Vegetarian", "Price (AED)": 30, "Rating": 4.5, "Mood": "Spicy"},
    {"Dish": "Schezwan Noodles", "Cuisine": "Chinese", "Diet": "Vegetarian", "Price (AED)": 32, "Rating": 4.4, "Mood": "Spicy"},
    {"Dish": "Veg Momos", "Cuisine": "Chinese", "Diet": "Vegetarian", "Price (AED)": 25, "Rating": 4.6, "Mood": "Comfort Food"},
    {"Dish": "Hot and Sour Soup", "Cuisine": "Chinese", "Diet": "Vegetarian", "Price (AED)": 18, "Rating": 4.2, "Mood": "Spicy"},

    # MIDDLE EASTERN
    {"Dish": "Falafel Wrap", "Cuisine": "Middle Eastern", "Diet": "Vegetarian", "Price (AED)": 20, "Rating": 4.5, "Mood": "Comfort Food"},
    {"Dish": "Hummus and Pita", "Cuisine": "Middle Eastern", "Diet": "Vegetarian", "Price (AED)": 25, "Rating": 4.4, "Mood": "Light"},
    {"Dish": "Veg Shawarma", "Cuisine": "Middle Eastern", "Diet": "Vegetarian", "Price (AED)": 30, "Rating": 4.3, "Mood": "Spicy"},
    {"Dish": "Fattoush Salad", "Cuisine": "Middle Eastern", "Diet": "Vegetarian", "Price (AED)": 25, "Rating": 4.2, "Mood": "Light"},
    {"Dish": "Vegetable Manakish", "Cuisine": "Middle Eastern", "Diet": "Vegetarian", "Price (AED)": 22, "Rating": 4.5, "Mood": "Cheesy"},
    {"Dish": "Baba Ganoush", "Cuisine": "Middle Eastern", "Diet": "Vegetarian", "Price (AED)": 20, "Rating": 4.3, "Mood": "Light"},
    {"Dish": "Falafel Platter", "Cuisine": "Middle Eastern", "Diet": "Vegetarian", "Price (AED)": 35, "Rating": 4.6, "Mood": "Comfort Food"},
    {"Dish": "Lentil Soup", "Cuisine": "Middle Eastern", "Diet": "Vegetarian", "Price (AED)": 18, "Rating": 4.4, "Mood": "Light"},
]


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
