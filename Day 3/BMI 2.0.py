# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi  = weight / (height **  2)

if bmi < 18.5:
    status = "are underweight"
if (bmi > 18.5) and (bmi < 25):
    status = "have a normal weight"
if (bmi > 25) and (bmi < 30):
    status = "are slightly overweight"
if (bmi > 30) and (bmi < 35):
    status = "are obese"
if (bmi > 35):
    status = "are clinically obese"
bmi = round(bmi)
print(f"Your BMI is {bmi}, you {status}.")
