# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
# https://waitbutwhy.com/2014/05/life-weeks.html
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.


# print welcoming message
print("\nWelcome to the life calculator\nPlease follow the steps below\n")

# capture user info
age = int(input("Please enter you age: "))
death_at = int(input("Please enter @ what age you'd like to die: "))

# calculate time remining based on 72 years
# there are 365 days in a year, 52 weeks in a year and 12 months in a year.

time_remaining = death_at - age

time_remaining_inDays = time_remaining * 365
time_remaining_inWeeks = time_remaining * 52
time_remaining_inMonths = time_remaining * 12

# print time remaining

print(f"You have:\n{time_remaining_inDays} days, ")
print(f"{time_remaining_inWeeks} weeks, or ")
print(f"{time_remaining_inMonths} months left.\n")
