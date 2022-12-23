help_row1 = ['11', '21', '31']
help_row2 = ['12', '22', '32']
help_row3 = ['13', '23', '33']

help_map = [
    help_row1,
    help_row2,
    help_row3
]

row1 = ['Hi', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

map = [
    row1, 
    row2,
    row3
]


user_selection = input("Where do you want to put the treasure?\n")
# print(user_selection)
# print(type(user_selection))
user_selection_row = int(user_selection[0])
# print(user_selection_row)
# print(type(user_selection_row))
user_selection_columns = int(user_selection[1])
# print(user_selection_columns)
# print(type(user_selection_columns))

print(map[user_selection_row][user_selection_columns])


