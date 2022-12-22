#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


# print welcome message 

print("Welcome to the tio calculator.")

# ask user for total bill, tip and split amount.

total_bill = float(input("What was the total bill? $"))
total_tip = float(input("What tip would you like to give? "))
total_clients = float(input("How many people to split the bill? "))

# calculate amount to pay

total_per_person = (total_bill / total_clients) * (1+(total_tip / 100))

# print total per person

print(f"Each person should pay: $ {round(total_per_person, 2)}\n")