print("Welcome to BMI Calculator 2.0")

# 🚨 Don't change the code below 👇
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round((weight / (height ** 2)), 1)
bmi_int = int(round(bmi))
'''
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
'''
message_bmi = f"Your BMI is {bmi_int}, "

if bmi < 18.5:
    explanation = "you are underweight."
elif bmi < 25:
    explanation = "you have a normal weight."
elif bmi < 30:
    explanation = "you are slightly overweight."
elif bmi < 35:
    explanation = "you are obese."
else:
    explanation = "you are clinically obese."

print(message_bmi + explanation)

'''SOLUTION
'''