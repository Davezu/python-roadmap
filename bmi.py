weight = float(input("Enter your weight (Ex:50) : "))
height = float(input("Enter your height (Ex:1.60 is 160cm) : "))

height = height / 100
    
compute_height = height * height

bmi = weight / compute_height

if bmi > 19 and 30:
    print(f"is BMI within the range? {True}, Your weight {weight}m and your height {height}cm, your BMI {bmi}")
else:
    print(f"is BMI within the range? {False}, Your weight {weight}m and your height {height}cm, your BMI {bmi}")
