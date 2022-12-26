#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

letter_selection = ""
number_selection = ""
symbol_selection = ""
password_raw = []
password = ""

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for _ in range(nr_letters):
    letter_selection_index = random.randint(0, (len(letters)-1)) # Index number selection for letters
    # Add letter selection to list
    password_raw.append(letters[letter_selection_index])

for _ in range(nr_numbers):
    number_selection_index = random.randint(0, (len(numbers)-1)) # Index number selection for numbers
    # Add number selection to list
    password_raw.append(numbers[number_selection_index])

for _ in range(nr_symbols):
    symbol_selection_index = random.randint(0, (len(symbols)-1)) # Index number selection for symbols
    # Add symbol selection to list
    password_raw.append(symbols[symbol_selection_index])

random.shuffle(password_raw) # Then change the order

# and convert it to str
for item in password_raw:
    password += item

# show the results to user
print(f"Here is your password: {password}")