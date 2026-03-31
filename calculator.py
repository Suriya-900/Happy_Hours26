import streamlit as st

# -------------------- CONFIG --------------------
st.set_page_config(page_title="Happy Hours Fitness", layout="centered")

# -------------------- SIDEBAR --------------------
st.sidebar.title("💃 Happy Hours")

page = st.sidebar.radio("Select Option", ["🔥 Calculator", "🥗 Diet Plan"])

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

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 10, 100)
        weight = st.number_input("Weight (kg)")
        target_weight = st.number_input("Target Weight (kg)")

    with col2:
        gender = st.selectbox("Gender", ["Male", "Female"])
        height = st.number_input("Height (cm)")
        days = st.number_input("Target Days")

    activity_level = st.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "Active"])

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🔥 Calculate"):

        st.markdown('<div class="card">', unsafe_allow_html=True)

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

        if weight_loss <= 0:
            st.error("Enter valid target weight")
        else:
            total_deficit = weight_loss * 7700
            daily_deficit = total_deficit / days
            target_calories = int(tdee - daily_deficit)

            st.subheader("🎯 Your Plan")
            st.write(f"📉 Daily deficit: **{int(daily_deficit)} kcal**")
            st.write(f"🍽️ Eat: **{target_calories} kcal/day**")

        st.markdown('</div>', unsafe_allow_html=True)
# =================================================
# 🥗 DIET PLAN PAGE
# =================================================
elif page == "🥗 Diet Plan":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🥗 Get Your Diet Plan")

    calories = st.number_input("Enter your daily calorie intake", min_value=500, max_value=4000, value=500)

    weight = st.number_input("Enter your weight (kg) for water intake", min_value=30, max_value=150, value=60)

    day = st.selectbox("Select Day", [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ])

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🍽️ Generate Diet Plan"):

        st.markdown('<div class="card">', unsafe_allow_html=True)

        # Water intake
        water = weight * 0.033  # liters

        st.subheader(f"🍽️ {day} Diet Plan (~{calories} kcal)")
        st.write(f"💧 Drink **{round(water,2)} liters** water daily")

        # Split calories
        morning = int(calories * 0.05)
        breakfast = int(calories * 0.2)
        snack1 = int(calories * 0.1)
        lunch = int(calories * 0.3)
        snack2 = int(calories * 0.1)
        dinner = int(calories * 0.25)

        # -------------------- MONDAY --------------------
        if day == "Monday":

            st.markdown("### 🌅 Morning Drink")
            st.write(f"Lemon water – 1 glass ({morning} kcal)")

            st.markdown("### 🍳 Breakfast")
            st.write(f"2 Idli (120g) + Sambar (150g) – ({breakfast} kcal)")

            st.markdown("### 🥜 Mid-Morning Snack")
            st.write(f"Sprouts salad (100g) – ({snack1} kcal)")

            st.markdown("### 🍛 Lunch")
            st.write(f"Rice (150g) + Dal (100g) + Veg curry – ({lunch} kcal)")

            st.markdown("### ☕ Evening Snack")
            st.write(f"2 Boiled eggs – ({snack2} kcal)")

            st.markdown("### 🍽️ Dinner")
            st.write(f"2 Chapati + Paneer curry (100g) – ({dinner} kcal)")

        # -------------------- TUESDAY --------------------
        elif day == "Tuesday":

            st.markdown("### 🌅 Morning Drink")
            st.write(f"Jeera water – ({morning} kcal)")

            st.markdown("### 🍳 Breakfast")
            st.write(f"2 Dosa + Chutney – ({breakfast} kcal)")

            st.markdown("### 🥜 Mid-Morning Snack")
            st.write(f"Fruit bowl (150g) – ({snack1} kcal)")

            st.markdown("### 🍛 Lunch")
            st.write(f"Rice + Sambar + Veg fry – ({lunch} kcal)")

            st.markdown("### ☕ Evening Snack")
            st.write(f"Chicken (100g) – ({snack2} kcal)")

            st.markdown("### 🍽️ Dinner")
            st.write(f"Chapati + Soya curry – ({dinner} kcal)")

        # -------------------- WEDNESDAY --------------------
        elif day == "Wednesday":

            st.markdown("### 🌅 Morning Drink")
            st.write(f"Warm water – ({morning} kcal)")

            st.markdown("### 🍳 Breakfast")
            st.write(f"Upma (200g) – ({breakfast} kcal)")

            st.markdown("### 🥜 Mid-Morning Snack")
            st.write(f"Groundnuts (30g) – ({snack1} kcal)")

            st.markdown("### 🍛 Lunch")
            st.write(f"Brown rice + Dal + Veg – ({lunch} kcal)")

            st.markdown("### ☕ Evening Snack")
            st.write(f"2 Eggs – ({snack2} kcal)")

            st.markdown("### 🍽️ Dinner")
            st.write(f"Chapati + Paneer – ({dinner} kcal)")

        # -------------------- THURSDAY --------------------
        elif day == "Thursday":

            st.markdown("### 🌅 Morning Drink")
            st.write(f"Lemon water – ({morning} kcal)")

            st.markdown("### 🍳 Breakfast")
            st.write(f"Pongal (200g) – ({breakfast} kcal)")

            st.markdown("### 🥜 Mid-Morning Snack")
            st.write(f"Sprouts – ({snack1} kcal)")

            st.markdown("### 🍛 Lunch")
            st.write(f"Rice + Veg curry – ({lunch} kcal)")

            st.markdown("### ☕ Evening Snack")
            st.write(f"Boiled egg – ({snack2} kcal)")

            st.markdown("### 🍽️ Dinner")
            st.write(f"Chapati + Chicken curry – ({dinner} kcal)")

        # -------------------- FRIDAY --------------------
        elif day == "Friday":

            st.markdown("### 🌅 Morning Drink")
            st.write(f"Jeera water – ({morning} kcal)")

            st.markdown("### 🍳 Breakfast")
            st.write(f"Dosa (2) – ({breakfast} kcal)")

            st.markdown("### 🥜 Mid-Morning Snack")
            st.write(f"Fruits – ({snack1} kcal)")

            st.markdown("### 🍛 Lunch")
            st.write(f"Rice + Dal + Veg – ({lunch} kcal)")

            st.markdown("### ☕ Evening Snack")
            st.write(f"Paneer (100g) – ({snack2} kcal)")

            st.markdown("### 🍽️ Dinner")
            st.write(f"Chapati + Soya – ({dinner} kcal)")

        # -------------------- SATURDAY --------------------
        elif day == "Saturday":

            st.markdown("### 🌅 Morning Drink")
            st.write(f"Warm water – ({morning} kcal)")

            st.markdown("### 🍳 Breakfast")
            st.write(f"Idli (2) – ({breakfast} kcal)")

            st.markdown("### 🥜 Mid-Morning Snack")
            st.write(f"Groundnuts – ({snack1} kcal)")

            st.markdown("### 🍛 Lunch")
            st.write(f"Rice + Chicken – ({lunch} kcal)")

            st.markdown("### ☕ Evening Snack")
            st.write(f"Egg – ({snack2} kcal)")

            st.markdown("### 🍽️ Dinner")
            st.write(f"Chapati + Paneer – ({dinner} kcal)")

        # -------------------- SUNDAY --------------------
        elif day == "Sunday":

            st.markdown("### 🌅 Morning Drink")
            st.write(f"Lemon water – ({morning} kcal)")

            st.markdown("### 🍳 Breakfast")
            st.write(f"Dosa (2) – ({breakfast} kcal)")

            st.markdown("### 🥜 Mid-Morning Snack")
            st.write(f"Fruits – ({snack1} kcal)")

            st.markdown("### 🍛 Lunch")
            st.write(f"Rice + Veg + Dal – ({lunch} kcal)")

            st.markdown("### ☕ Evening Snack")
            st.write(f"Chicken – ({snack2} kcal)")

            st.markdown("### 🍽️ Dinner")
            st.write(f"Chapati + Soya – ({dinner} kcal)")

        st.markdown('</div>', unsafe_allow_html=True)