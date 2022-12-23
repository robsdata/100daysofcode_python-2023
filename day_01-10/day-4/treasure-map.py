# Instructions
# You are going to write a program that will mark a spot with an X.

# In the starting code, you will find a variable called map.

# This map contains a nested list. When map is printed this is what the nested list looks like:

# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}" to format the 3 lists to be printed as a 3 by 3 square, each on a new line. 

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']


# Your job is to write a program that allows you to mark a square on the map using a two-digit system. 

# The first digit in the input will specify the column (the position on the horizontal axis).

# The second digit in the input will specify the row number (the position on the vertical axis). 


row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

map = [
    row1, 
    row2,
    row3
]

try:
    user_selection = input("Where do you want to put the treasure?\n")
    # print(user_selection)
    # print(type(user_selection))
    user_selection_row = int(user_selection[0])
    # print(user_selection_row)
    # print(type(user_selection_row))
    user_selection_columns = int(user_selection[1])
    # print(user_selection_columns)
    # print(type(user_selection_columns))

    map[user_selection_row][user_selection_columns] = "X"
    print(f"{row1}\n{row2}\n{row3}")

except:
    print("Wrong entry")
