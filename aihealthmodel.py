def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Healthy weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_calories(gender, weight, height, age, activity_level):
    height_cm = height * 100
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height_cm - 5 * age - 161

    multipliers = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725,
        5: 1.9
    }

    return bmr * multipliers.get(activity_level, 1.2)

def fitness_advice(bmi):
    if bmi < 18.5:
        return "You may benefit from strength training and increasing calorie intake."
    elif 18.5 <= bmi < 25:
        return "Great job! A balanced diet and regular exercise will keep you on track."
    elif 25 <= bmi < 30:
        return "Consider mixing cardio and strength training while managing calorie intake."
    else:
        return "A structured fitness plan and nutrition focus may help—small steps matter."

print("AI Fitness & Health Calculator\n")

gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters (e.g., 1.75): "))

print("\nActivity Levels:")
print("1 = Not active")
print("2 = Light exercise 1–3 days/week")
print("3 = Moderate exercise 3–5 days/week")
print("4 = Hard exercise 6–7 days/week")
print("5 = Athlete training")
activity_level = int(input("Choose your activity level (1–5): "))

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)
calories = calculate_calories(gender, weight, height, age, activity_level)
advice = fitness_advice(bmi)

print("\n--------- Your Health Report ---------")
print(f"BMI: {bmi:.2f} ({category})")
print(f"Daily Calorie Needs: {calories:.0f} kcal")
print(f"Advice: {advice}")
print("--------------------------------------")

