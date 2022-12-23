# Instructions
# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.

# Example Output
# Michael is going to buy the meal today!

import random

# Ask user for names
names_string = input("Type the name of the players separated by a comma (,) and space:\n------> ")

# and then, convert the str to a list
names_list = names_string.split(", ")
# print(type(names_list))
# print(len(names_list))

# Select a random number from 0 to count of list names
system_selection = random.randint(0, (len(names_list)-1))

# Show results to user
print(f"{names_list[system_selection]} is going to buy the meal today")
