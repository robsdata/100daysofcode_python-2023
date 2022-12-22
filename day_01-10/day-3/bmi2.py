# Instructions
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# - Under 18.5 they are underweight
# - Over 18.5 but below 25 they have a normal weight
# - Over 25 but below 30 they are slightly overweight
# - Over 30 but below 35 they are obese
# - Above 35 they are clinically obese.


# Print welcoming message
print("Welcome to the bmi calculator!")

# Ask user for input (weight, height)
user_weight = float(input("Please enter your weight (kg) ---> "))
user_height = float(input("Please enter your height (m) ---> "))

# Perform bmi calculation
bmi = round(user_weight / user_height**2, 1)

# Return user message based on bmi

if bmi < 18.5:
    #underweight
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi < 25:
    #normal
    print(f"Your bmi is {bmi}, you are normal")
elif bmi < 30:
    #slightly overweight
    print(f"Your bmi is {bmi}, you are slightly overweight")
elif bmi < 35:
    #obese
    print(f"Your bmi is {bmi}, you are obese")
else:
    #clinical obese
    print(f"Your bmi is {bmi}, you are clinical obese")