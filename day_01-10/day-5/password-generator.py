#Password Generator Project
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter_selection = ""
number_selection = ""
symbol_selection = ""
password = ""


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for _ in range(nr_letters):
    letter_selection = random.randint(0, (len(letters)-1)) # Index number selection for letters
    password += letters[letter_selection]

for _ in range(nr_numbers):
    letter_selection = random.randint(0, (len(numbers)-1)) # Index number selection for numbers
    password += numbers[letter_selection]

for _ in range(nr_symbols):
    letter_selection = random.randint(0, (len(symbols)-1)) # Index number selection for symbols
    password += symbols[letter_selection]

print(f"Here is your password: {password}")