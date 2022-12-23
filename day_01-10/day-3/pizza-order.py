
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.

# creating variables

# messages
pepperoni_offer_message_small = "Pepperoni for Small Pizza: +$2"
pepperoni_offer_message_l_m = "Pepperoni for Medium or Large Pizza: +$3"
pepperoni_offer_message = "nothing selected"

# pizza size selection
user_selection = ""    
peperoni_selection = ""
cheese_selection = ""

# pizza prices
small_pizza_price = 15.0
medium_pizza_price = 20.0
large_pizza_price = 25.0

# peperoni prices
perperoni_small_pizza_price = 2.0
perperoni_m_l_pizza_price = 3.0

# extras
extra_cheese_price = 1.0


# assign 0.0 to total bill
total_bill = 0.0

# print welcoming message & menu
print("---- Welcome to the pizza order system ----\n")
print("---- Menu ----")
print("(S) Small Pizza: $15")
print("(M) Medium Pizza: $20")
print("(L) Large Pizza: $25")

# ask for user selection pizza size
# and assign pizza price

user_selection = input("\n( S / M / L )---> ").upper()

if user_selection == "S":
    total_bill += small_pizza_price
    pepperoni_offer_message = pepperoni_offer_message_small
    print("---small selected---")

elif user_selection == "M" or user_selection == "L":
    pepperoni_offer_message = pepperoni_offer_message_l_m

    if user_selection == "M":
        total_bill += medium_pizza_price
        print("---medium selected---")
    elif user_selection == "L":
        total_bill += large_pizza_price
        print("---large selected---")
    else:
        print("---error---")
else:
    print("Wrong entry") # Display message for wrong entry


# if the usern has an active selection
if user_selection == "S" or user_selection == "M" or user_selection == "L":
    # ask user if wants to add pepperoni
    peperoni_selection = input(f"add pepperoni to your order?\n{pepperoni_offer_message}\n( Y / N )---> ").upper()
    if peperoni_selection == "Y" and user_selection == "S":
        total_bill += perperoni_small_pizza_price # if the pizza is small, charge small price
        print("---charged small pepperoni---")
    elif peperoni_selection == "Y" and (user_selection == "M" or user_selection == "L"):
        total_bill += perperoni_m_l_pizza_price # if the pizza is large, or medium charge price
        print("---charged large/medium pepperoni---")
    else:
        print("Peperoni not added") # else, let the client know

    #ask client if extra cheese should be added
    cheese_selection = input("Extra cheese for any size pizza: + $1\n( Y / N )---> ").upper()

    # if the client wants cheese
    if cheese_selection == "Y":
        total_bill += extra_cheese_price # charge extra cheese
        print("---charged extra cheese---")

    # print grand total
    print(f"Your total is...\n$ {total_bill}\nThank you for using this system.")