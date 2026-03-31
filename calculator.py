import streamlit as st
import pandas as pd
from datetime import datetime
import os


# -------------------- CONFIG --------------------
st.set_page_config(page_title="Happy Hours Fitness", layout="centered")


# ---------------- SIDEBAR ----------------
st.sidebar.title("Menu")
page = st.sidebar.radio("Select Page", ["🔥 Calculator", "🥗 Diet Plan", "📊 Tracker"])

# -------------------- COMMON UI --------------------
st.markdown("""
<style>
.title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: #ff4b4b;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💃 Happy Hours Move & Groove</div>', unsafe_allow_html=True)

# =================================================
# 🔥 CALCULATOR PAGE
# =================================================
if page == "🔥 Calculator":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🧾 Enter Your Details")

    name = st.text_input("Name")
    phone = st.text_input("Phone Number")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 10, 100)
        weight = st.number_input("Weight (kg)")
        target_weight = st.number_input("Target Weight (kg)")

    with col2:
        gender = st.selectbox("Gender", ["Male", "Female"])
        height = st.number_input("Height (cm)")
        days = st.number_input("Target Days", min_value=1, value=30)

    activity_level = st.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "Active"])

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🔥 Calculate"):

        st.markdown('<div class="card">', unsafe_allow_html=True)

        # Validate name and phone
        if not name.strip() or not phone.strip():
            st.error("Please enter Name and Phone to continue.")
        else:

            # BMI
            h = height / 100
            bmi = weight / (h*h)

            st.subheader("📊 Your BMI")
            st.write(f"**{round(bmi,1)}**")

            if bmi < 18.5:
                st.info("Underweight")
            elif bmi < 25:
                st.success("Normal weight")
            elif bmi < 30:
                st.warning("Overweight")
            else:
                st.error("Obese")

            # BMR
            if gender == "Male":
                bmr = 10*weight + 6.25*height - 5*age + 5
            else:
                bmr = 10*weight + 6.25*height - 5*age - 161

            activity_map = {
                "Sedentary": 1.2,
                "Light": 1.375,
                "Moderate": 1.55,
                "Active": 1.725
            }

            tdee = bmr * activity_map[activity_level]

            st.subheader("🔥 Daily Calories")
            st.write(f"Maintain weight: **{int(tdee)} kcal/day**")

            # Weight loss
            weight_loss = weight - target_weight
            target_calories = None

            if weight_loss <= 0:
                st.error("Target weight must be less than current weight.")
            else:
                total_deficit = weight_loss * 7700
                daily_deficit = total_deficit / days
                target_calories = int(tdee - daily_deficit)

                st.subheader("🎯 Your Plan")
                st.write(f"📉 Daily deficit: **{int(daily_deficit)} kcal**")
                st.write(f"🍽️ Eat: **{target_calories} kcal/day**")

            # SAVE DATA ONLY IF target_calories IS DEFINED
            if target_calories is not None:
                data = {
                    "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Name": name,
                    "Phone": phone,
                    "Weight": weight,
                    "Target Weight": target_weight,
                    "Calories Target": target_calories
                }

                df = pd.DataFrame([data])

                if os.path.exists("calculator_data.csv"):
                    df.to_csv("calculator_data.csv", mode='a', header=False, index=False)
                else:
                    df.to_csv("calculator_data.csv", index=False)

        st.markdown('</div>', unsafe_allow_html=True)

# =================================================
# 🥗 DIET PLAN PAGE
# =================================================
elif page == "🥗 Diet Plan":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🥗 Get Your Diet Plan")

    calories = st.number_input("Enter your daily calorie intake", min_value=500, max_value=4000, value=1500)

    weight = st.number_input("Enter your weight (kg) for water intake", min_value=10, max_value=150, value=60)

    day = st.selectbox("Select Day", [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ])

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🍽️ Generate Diet Plan"):

        st.markdown('<div class="card">', unsafe_allow_html=True)

        water = weight * 0.033  

        st.subheader(f"🍽️ {day} Diet Plan (~{calories} kcal)")
        st.write(f"💧 Drink **{round(water,2)} liters** water daily")

        morning = int(calories * 0.05)
        breakfast = int(calories * 0.2)
        snack1 = int(calories * 0.1)
        lunch = int(calories * 0.3)
        snack2 = int(calories * 0.1)
        dinner = int(calories * 0.25)

        # Meal plan per day
        meal_plan = {
            "Monday": [
                ("🌅 Morning Drink", f"Lemon water – 1 glass ({morning} kcal)"),
                ("🍳 Breakfast", f"2 Idli (120g) + Sambar (150g) – ({breakfast} kcal)"),
                ("🥜 Mid-Morning Snack", f"Sprouts salad (100g) – ({snack1} kcal)"),
                ("🍛 Lunch", f"Rice (150g) + Dal (100g) + Veg curry – ({lunch} kcal)"),
                ("☕ Evening Snack", f"2 Boiled eggs – ({snack2} kcal)"),
                ("🍽️ Dinner", f"2 Chapati + Paneer curry (100g) – ({dinner} kcal)")
            ],
            "Tuesday": [
                ("🌅 Morning Drink", f"Jeera water – ({morning} kcal)"),
                ("🍳 Breakfast", f"2 Dosa + Chutney – ({breakfast} kcal)"),
                ("🥜 Mid-Morning Snack", f"Fruit bowl (150g) – ({snack1} kcal)"),
                ("🍛 Lunch", f"Rice + Sambar + Veg fry – ({lunch} kcal)"),
                ("☕ Evening Snack", f"Chicken (100g) – ({snack2} kcal)"),
                ("🍽️ Dinner", f"Chapati + Soya curry – ({dinner} kcal)")
            ],
            "Wednesday": [
                ("🌅 Morning Drink", f"Warm water – ({morning} kcal)"),
                ("🍳 Breakfast", f"Upma (200g) – ({breakfast} kcal)"),
                ("🥜 Mid-Morning Snack", f"Groundnuts (30g) – ({snack1} kcal)"),
                ("🍛 Lunch", f"Brown rice + Dal + Veg – ({lunch} kcal)"),
                ("☕ Evening Snack", f"2 Eggs – ({snack2} kcal)"),
                ("🍽️ Dinner", f"Chapati + Paneer – ({dinner} kcal)")
            ],
            "Thursday": [
                ("🌅 Morning Drink", f"Lemon water – ({morning} kcal)"),
                ("🍳 Breakfast", f"Pongal (200g) – ({breakfast} kcal)"),
                ("🥜 Mid-Morning Snack", f"Sprouts – ({snack1} kcal)"),
                ("🍛 Lunch", f"Rice + Veg curry – ({lunch} kcal)"),
                ("☕ Evening Snack", f"Boiled egg – ({snack2} kcal)"),
                ("🍽️ Dinner", f"Chapati + Chicken curry – ({dinner} kcal)")
            ],
            "Friday": [
                ("🌅 Morning Drink", f"Jeera water – ({morning} kcal)"),
                ("🍳 Breakfast", f"Dosa (2) – ({breakfast} kcal)"),
                ("🥜 Mid-Morning Snack", f"Fruits – ({snack1} kcal)"),
                ("🍛 Lunch", f"Rice + Dal + Veg – ({lunch} kcal)"),
                ("☕ Evening Snack", f"Paneer (100g) – ({snack2} kcal)"),
                ("🍽️ Dinner", f"Chapati + Soya – ({dinner} kcal)")
            ],
            "Saturday": [
                ("🌅 Morning Drink", f"Warm water – ({morning} kcal)"),
                ("🍳 Breakfast", f"Idli (2) – ({breakfast} kcal)"),
                ("🥜 Mid-Morning Snack", f"Groundnuts – ({snack1} kcal)"),
                ("🍛 Lunch", f"Rice + Chicken – ({lunch} kcal)"),
                ("☕ Evening Snack", f"Egg – ({snack2} kcal)"),
                ("🍽️ Dinner", f"Chapati + Paneer – ({dinner} kcal)")
            ],
            "Sunday": [
                ("🌅 Morning Drink", f"Lemon water – ({morning} kcal)"),
                ("🍳 Breakfast", f"Dosa (2) – ({breakfast} kcal)"),
                ("🥜 Mid-Morning Snack", f"Fruits – ({snack1} kcal)"),
                ("🍛 Lunch", f"Rice + Veg + Dal – ({lunch} kcal)"),
                ("☕ Evening Snack", f"Chicken – ({snack2} kcal)"),
                ("🍽️ Dinner", f"Chapati + Soya – ({dinner} kcal)")
            ]
        }

        for title, meal in meal_plan[day]:
            st.markdown(f"### {title}")
            st.write(meal)

        st.markdown('</div>', unsafe_allow_html=True)

# =================================================
# 📊 TRACKER PAGE
# =================================================
elif page == "📊 Tracker":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📊 Daily Tracker")

    name = st.text_input("Name")
    phone = st.text_input("Phone Number")

    intake = st.number_input("Calories Consumed", value=0)
    burned = st.number_input("Calories Burned", value=0)

    st.markdown("### 🍔 Cheat Meal")
    cheat = st.checkbox("Had Cheat Meal?")

    extra = 0
    cheat_food = "No"

    if cheat:
        cheat_food = st.selectbox("Food", ["Biryani", "Pizza", "Burger"])

        if cheat_food == "Biryani":
            qty = st.selectbox("Qty", ["1 Plate", "2 Plates"])
            extra = 700 if qty == "1 Plate" else 1400

        elif cheat_food == "Pizza":
            qty = st.selectbox("Slices", ["2", "4", "6"])
            extra = int(qty) * 250

        elif cheat_food == "Burger":
            qty = st.selectbox("Qty", ["1", "2"])
            extra = int(qty) * 300

        st.info(f"Extra Calories: {extra}")

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Save Today"):

        # Validate name and phone
        if not name.strip() or not phone.strip():
            st.error("Please enter Name and Phone to save data.")
        else:
            total = intake + extra
            net = total - burned

            st.write(f"Net Calories: {net}")

            if net < 0:
                weight_loss = abs(net) / 7700
            else:
                weight_loss = 0

            st.write(f"Approx Weight Loss: {round(weight_loss,4)} kg")
            st.caption("⚠️ Approx only. Depends on body.")

            data = {
                "Date": datetime.now().strftime("%Y-%m-%d"),
                "Name": name,
                "Phone": phone,
                "Intake": total,
                "Burned": burned,
                "Net": net,
                "Cheat": cheat_food,
                "Extra": extra,
                "Weight_Loss": round(weight_loss,4)
            }

            df = pd.DataFrame([data])

            if os.path.exists("tracker_data.csv"):
                df.to_csv("tracker_data.csv", mode="a", header=False, index=False)
            else:
                df.to_csv("tracker_data.csv", index=False)

    st.markdown("### 📅 History")

    if os.path.exists("tracker_data.csv"):
        df = pd.read_csv("tracker_data.csv")
        st.dataframe(df)
        st.line_chart(df["Weight_Loss"])
    else:
        st.info("No data yet")