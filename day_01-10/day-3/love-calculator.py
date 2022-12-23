# Instructions
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:

# variables
t_true_count = 0
r_true_count = 0
u_true_count = 0
e_true_count = 0

l_love_count = 0
o_love_count = 0
v_love_count = 0
e_love_count = 0

true_total_count = 0
love_total_count = 0

love_digit = ""


# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
name_person1 = input("Please enter your name --->").lower()
name_person2 = input("Please enter your SO's name --->").lower()

# Then check for the number of times the letters in the word TRUE LOVE occurs. 

t_true_count = name_person1.count("t") + name_person2.count("t")
r_true_count = name_person1.count("r") + name_person2.count("r")
u_true_count = name_person1.count("u") + name_person2.count("u")
e_true_count = name_person1.count("e") + name_person2.count("e")

l_love_count = name_person1.count("l") + name_person2.count("l")
o_love_count = name_person1.count("o") + name_person2.count("o")
v_love_count = name_person1.count("v") + name_person2.count("v")
e_love_count = name_person1.count("e") + name_person2.count("e")

true_total_count = t_true_count + r_true_count + u_true_count + e_true_count
love_total_count = l_love_count + o_love_count + v_love_count + e_love_count
# print("TRUE -----------------")
# print(t_true_count)
# print(r_true_count)
# print(u_true_count)
# print(e_true_count)
# print(" LOVE-----------------")
# print(l_love_count)
# print(o_love_count)
# print(v_love_count)
# print(e_love_count)
# print("TOTAL-----------------")
# print(true_total_count)
# print(love_total_count)



# Then combine these numbers to make a 2 digit number.
love_digit = str(true_total_count) + str(love_total_count)
love_digit = int(love_digit)
# print(type(love_digit))
# print(love_digit)



# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
if love_digit < 10 or love_digit > 90:
    print(f"Your score is {love_digit}, you go together like coke and mentos")

# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
elif love_digit > 40 and love_digit < 50:
    print(f"Your score is {love_digit}, you are alright together.")

# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."
else:
    print(f"Your score is {love_digit}")