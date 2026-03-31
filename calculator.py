import streamlit as st

# Page config
st.set_page_config(page_title="Happy Hours Fitness", layout="centered")

# Custom styling
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fc;
    }
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #ff4b4b;
    }
    .subtext {
        text-align: center;
        font-size: 16px;
        color: gray;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">💃 Happy Hours Move & Groove</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Dance • Burn Calories • Stay Fit</div>', unsafe_allow_html=True)
st.write("")

# Inputs Card
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

workout = st.selectbox("Preferred Activity", ["Walking", "Dance", "Yoga", "Exercise"])
hours = st.number_input("Hours per day", min_value=0.5, max_value=5.0, value=1.0)

st.markdown('</div>', unsafe_allow_html=True)

# Button
if st.button("🔥 Calculate My Plan"):

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

    # TDEE
    if activity_level == "Sedentary":
        tdee = bmr * 1.2
    elif activity_level == "Light":
        tdee = bmr * 1.375
    elif activity_level == "Moderate":
        tdee = bmr * 1.55
    else:
        tdee = bmr * 1.725

    st.subheader("🔥 Daily Calories")
    st.write(f"To maintain weight: **{int(tdee)} kcal/day**")

    # Weight loss
    weight_loss = weight - target_weight

    if weight_loss <= 0:
        st.error("Please enter a valid target weight")
    else:
        total_deficit = weight_loss * 7700
        daily_deficit = total_deficit / days

        target_calories = tdee - daily_deficit

        st.subheader("🎯 Your Plan")
        st.write(f"📉 Daily deficit: **{int(daily_deficit)} kcal**")
        st.write(f"🍽️ Eat: **{int(target_calories)} kcal/day**")

        if target_calories < 1200:
            st.warning("Increase your timeline for better results")

    st.markdown('</div>', unsafe_allow_html=True)

    # Activity Card
    st.markdown('<div class="card">', unsafe_allow_html=True)

    burn_dict = {
        "Walking": 200,
        "Dance": 300,
        "Yoga": 180,
        "Exercise": 400
    }

    burn_per_hour = burn_dict[workout]
    total_burn = burn_per_hour * hours

    st.subheader("💃 Your Activity")

    st.write(f"{workout} for **{hours} hours/day**")
    st.write(f"🔥 Burns: **{int(total_burn)} kcal/day**")

    st.success("This will help you lose weight faster 🚀")

    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.info("💡 Eat smart + Stay active = Best results 💯")