height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height * height)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, your are underweight")
elif bmi < 25:
    print(f"Your BMi is {bmi}, your are normal weight")
elif bmi < 30:
    print(f"your BMi is {bmi}, your are overweight")
elif bmi < 35:
    print(f"your BMi is {bmi}, your are obese")
else:
    print(f"yoru BMI is {bmi}, your are clinically obese")