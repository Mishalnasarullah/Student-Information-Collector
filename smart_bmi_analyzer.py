print("=" * 50)
print("     SMART BMI & HEALTH ANALYZER")
print("=" * 50)

# Part 1 - Collect Patient Information
name = input("Enter Patient Name: ")
age = int(input("Enter Age (Years): "))
weight = float(input("Enter Weight (Kilograms): "))
height = float(input("Enter Height (Meters): "))

# Part 2 - Calculate BMI
bmi = weight / (height * height)

# Part 3 - Determine BMI Category
if bmi < 18.5:
    category = "Underweight"
    recommendation = "Increase calorie intake and consult a nutritionist."

elif bmi >= 18.5 and bmi <= 24.9:
    category = "Normal Weight"
    recommendation = "Maintain your current healthy lifestyle."

elif bmi >= 25 and bmi <= 29.9:
    category = "Overweight"
    recommendation = "Increase physical activity and improve diet."

else:
    category = "Obese"
    recommendation = "Consult a healthcare professional and follow a weight management plan."

# Part 4 - Assess Health Risk (Nested if-else)
if bmi > 30:
    if age > 40:
        health_risk = "High Health Risk"
    else:
        health_risk = "Normal Risk"
else:
    health_risk = "Normal Risk"

# Bonus Challenge 1 - Daily Water Intake
water_intake = weight * 35

# Bonus Challenge 2 - Weight Difference Calculator
ideal_weight = 22 * (height * height)
weight_difference = weight - ideal_weight

# Part 5 - Health Report
print()
print("=" * 50)
print("            HEALTH REPORT")
print("=" * 50)

print(f"Patient Name : {name}")
print(f"Age : {age} Years")
print(f"Weight : {weight} kg")
print(f"Height : {height} m")
print(f"Calculated BMI : {bmi:.2f}")
print(f"BMI Category : {category}")
print(f"Health Risk : {health_risk}")
print(f"Recommended Water Intake : {water_intake} ml/day")
print(f"Current Weight : {weight} kg")
print(f"Ideal Weight : {ideal_weight} kg")
print(f"Weight Difference : {weight_difference} kg")

print()
print("Health Recommendation")
print(recommendation)

print("=" * 50)
print("Thank you for using Smart BMI & Health Risk Analyzer")
print("=" * 50)