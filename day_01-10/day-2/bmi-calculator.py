# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# BMI = weight / height * height 


# Print welcoming message
print("\nWelcome to the BMI calculator\nPlease enter the required information\n\n")

# then capture information from user
weight = float(input("Please enter your weight: \n"))
height = float(input("Please enter your height: \n"))

# calculate bmi
bmi = weight / height**2

# print results
print(f"\nYour bmi result is: {round(bmi, 1)}")