import pandas as pd
import os
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    # ---------------- INPUTS ----------------
    sleep = float(request.form["sleep"])
    water = float(request.form["water"])
    screen = float(request.form["screen"])
    walk = float(request.form["walk"])
    stress = float(request.form["stress"])
    weight = float(request.form["weight"])
    height_cm = float(request.form["height"])
    calories = float(request.form["calories"])
    mood = request.form["mood"].lower()
    medicine = request.form["medicine"].lower()

    height = height_cm / 100

    # ---------------- HEALTH SCORE ----------------
    score = 100

    if sleep < 7:
        score -= 10
    if water < 2:
        score -= 10
    if screen > 6:
        score -= 10
    if walk < 30:
        score -= 10
    if stress > 3:
        score -= 15

    if score < 0:
        score = 0

    # ---------------- HEALTH GRADE ----------------
    if score >= 85:
        grade = "A+ Excellent"
    elif score >= 70:
        grade = "B Good"
    elif score >= 50:
        grade = "C Needs Improvement"
    else:
        grade = "D Health Risk"

    # ---------------- BMI ----------------
    bmi = round(weight / (height ** 2), 2)

    if bmi < 18.5:
        bmi_status = "Underweight"
    elif bmi < 25:
        bmi_status = "Normal"
    elif bmi < 30:
        bmi_status = "Overweight"
    else:
        bmi_status = "Obese"

    # ---------------- CALORIE STATUS ----------------
    if calories < 1200:
        calorie_status = "Very Low Calorie Intake"
    elif calories > 2500:
        calorie_status = "High Calorie Intake"
    else:
        calorie_status = "Normal Calorie Intake"

    # ---------------- HYDRATION ----------------
    hydration = min(int((water / 3) * 100), 100)

    if water < 1.5:
        dehydration_alert = "Dehydration Risk"
    else:
        dehydration_alert = "Hydration Level Acceptable"

    # ---------------- SCREEN ADDICTION ----------------
    if screen > 8:
        screen_risk = "High Screen Addiction Risk"
    elif screen > 6:
        screen_risk = "Moderate Screen Usage"
    else:
        screen_risk = "Healthy Screen Time"

    # ---------------- BURNOUT ----------------
    if stress >= 4 and sleep < 6:
        burnout = "High Risk"
    elif stress >= 3:
        burnout = "Moderate"
    else:
        burnout = "Low"

    # ---------------- MENTAL SCORE ----------------
    mental_score = 100

    if stress > 3:
        mental_score -= 20
    if mood == "sad":
        mental_score -= 20
    if sleep < 6:
        mental_score -= 10

    # ---------------- MOOD MESSAGE ----------------
    if mood == "sad":
        mood_msg = "Try light music or talk to a friend."
    elif mood == "stressed":
        mood_msg = "Practice deep breathing for 5 minutes."
    else:
        mood_msg = "Maintain your positive mindset."

    # ---------------- MEDICINE TRACKER ----------------
    if medicine == "yes":
        medicine_msg = "Medicine taken correctly."
    else:
        medicine_msg = "Reminder: Take medicine on time."

    # ---------------- DAILY ACTION PLAN ----------------
    actions = []

    if sleep < 7:
        actions.append("Sleep before 11 PM")
    if water < 2:
        actions.append("Drink 2 more glasses of water")
    if walk < 30:
        actions.append("Walk 20 minutes in evening")
    if stress > 3:
        actions.append("Do 5 min breathing exercise")

    if not actions:
        actions.append("Maintain current healthy routine")

    daily_plan = " | ".join(actions)

    # ---------------- REMINDER ----------------
    reminder = ""
    if water < 2:
        reminder += "Drink water every 2 hours. "
    if sleep < 7:
        reminder += "Sleep before 11 PM. "
    if walk < 30:
        reminder += "Evening walk reminder. "

    if reminder == "":
        reminder = "No reminder needed today."

    # ---------------- SAVE DAILY LOG ----------------
    today = datetime.now().strftime("%Y-%m-%d")

    entry = {
        "date": today,
        "sleep": sleep,
        "water": water,
        "stress": stress
    }

    file = "daily_log.csv"

    if os.path.exists(file):
        df = pd.read_csv(file)
        df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    else:
        df = pd.DataFrame([entry])

    df.to_csv(file, index=False)

    # ---------------- WEEKLY TREND ----------------
    recent = df.tail(7)

    avg_sleep = recent["sleep"].mean()
    avg_stress = recent["stress"].mean()

    improvement = ""

    if avg_sleep < 6:
        improvement += "Improve sleep consistency. "
    if avg_stress > 3:
        improvement += "Stress trend increasing. "

    if improvement == "":
        improvement = "Great weekly stability."

    # ---------------- RESULT LABEL ----------------
    if score >= 70:
        result = "Healthy"
        reason = "Your lifestyle is mostly balanced."
    else:
        result = "Needs Attention"
        reason = "Some habits need improvement."

    return render_template("index.html",
                           result=result,
                           reason=reason,
                           score=score,
                           grade=grade,
                           bmi=bmi,
                           bmi_status=bmi_status,
                           hydration=hydration,
                           burnout=burnout,
                           calorie_status=calorie_status,
                           screen_risk=screen_risk,
                           dehydration_alert=dehydration_alert,
                           mental_score=mental_score,
                           daily_plan=daily_plan,
                           reminder=reminder,
                           improvement=improvement,
                           mood_msg=mood_msg,
                           medicine_msg=medicine_msg)

if __name__ == "__main__":
    app.run(debug=True)

 