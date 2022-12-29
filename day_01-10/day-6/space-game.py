
def finilizing_game(game_result):
    winning_message = '''
            __
        | \
        =[_|H)--._____
        =[+--,-------'
        [|_/""        robsdata-sv

        🧑‍🚀: YOU WIN!!!!

    '''

    failed_message = '''
    YOU LOOSE!

    ⣀⣠⣤⣤⣤⣤⢤⣤⣄⣀⣀⣀⣀⡀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
    ⠄⠉⠹⣾⣿⣛⣿⣿⣞⣿⣛⣺⣻⢾⣾⣿⣿⣿⣶⣶⣶⣄⡀⠄⠄⠄
    ⠄⠄⠠⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣆⠄⠄
    ⠄⠄⠘⠛⠛⠛⠛⠋⠿⣷⣿⣿⡿⣿⢿⠟⠟⠟⠻⠻⣿⣿⣿⣿⡀⠄
    ⠄⢀⠄⠄⠄⠄⠄⠄⠄⠄⢛⣿⣁⠄⠄⠒⠂⠄⠄⣀⣰⣿⣿⣿⣿⡀
    ⠄⠉⠛⠺⢶⣷⡶⠃⠄⠄⠨⣿⣿⡇⠄⡺⣾⣾⣾⣿⣿⣿⣿⣽⣿⣿
    ⠄⠄⠄⠄⠄⠛⠁⠄⠄⠄⢀⣿⣿⣧⡀⠄⠹⣿⣿⣿⣿⣿⡿⣿⣻⣿
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠛⠟⠇⢀⢰⣿⣿⣿⣏⠉⢿⣽⢿⡏
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠤⣤⣴⣾⣿⣿⣾⣿⣿⣦⠄⢹⡿⠄
    ⠄⠄⠄⠄⠄⠄⠄⠄⠒⣳⣶⣤⣤⣄⣀⣀⡈⣀⢁⢁⢁⣈⣄⢐⠃⠄
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⣰⣿⣛⣻⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⣬⣽⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⢘⣿⣿⣻⣛⣿⡿⣟⣻⣿⣿⣿⣿⡟⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠛⢛⢿⣿⣿⣿⣿⣿⣿⣷⡿⠁⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠉⠉⠈⠄⠄⠄⠄⠄⠄

    '''
    
    if game_result == True:
        print(winning_message)
    else:
        print(failed_message)

def update_game_map(index_columns, index_row, last_index_columns ,last_index_row):
    
    player = "🤖"
    star = "⭐" * 24
    
    game_map[index_columns][index_row] = player
    game_map[last_index_columns][last_index_row] = "  "
    print(f"{star}\n\n{row1}\n{row2}\n\n{star}")

def game_check(is_game_running, is_inside_columns, is_inside_rows, position_columns, position_rows, user_wins):
    print(f"\nIs inside columns: {is_inside_columns}, and position is ({position_columns}, {position_rows})")
    print(f"Is inside rows: {is_inside_rows}")
    print(f"Game running = {is_game_running}")
    print(f"User wins = {user_wins}\n")


star = "🔥"
goal = "🏁"

# creating game map
row1 = [
    star, "  ",  "  ", "  ", star, "  ", "  ", "  "
]
row2 = [
    "  ", "  ", star, "  ", "  ", "  ", star,  goal
]
game_map = [
    row1, 
    row2,
    ]

# game variables

is_game_running = True
user_wins = False
is_inside_rows = True
is_inside_columns = True


# player position starts at
# up & down
position_columns = 1 # only values 0 or 1 ; index 1 = win
# left & right
position_rows = 0 # only values < 7 ; index 7 = win

# Initialize vcariables to save last index position
last_position_columns = 1
last_position_rows = 0



while  is_game_running == True:
    # Ask user for input "A", "D" to control rows, "W", "S" to control columns
    user_selection = input("Please enter your move selection:\n(A)to move left\n(W)to move up\n(S)to move down\n(D)to move right\n").lower()

    # Based on user's input move player
    # Rows
    if user_selection == 'a':
        # move left
        last_position_rows = position_rows
        last_position_columns = position_columns
        position_rows -= 1
    elif user_selection == 'd':
        # move right
        last_position_rows = position_rows
        last_position_columns = position_columns
        position_rows += 1
    
    # columns
    elif user_selection == 'w':
        # move up
        last_position_columns = position_columns
        last_position_rows = position_rows
        position_columns -= 1
    elif user_selection == 's':
        #move down
        last_position_columns = position_columns
        last_position_rows = position_rows
        position_columns += 1
    
    # Wrong Entry
    else:
        print("\nWrong entry\n")



    # Check for constraints and actions
    # If user is in position (7, 1) then the user wins
    if position_rows == 7 and position_columns == 1:
        is_game_running = False
        user_wins = True
    
    # Vertical Check
    elif (position_columns > 1) or (position_columns < 0):
        is_game_running = False
        is_inside_columns = False
        user_wins = False
    
    # Horizontal Check
    elif (position_rows < 0) or (position_rows > 7):
        is_game_running = False
        is_inside_rows = False
        user_wins = False

    if is_game_running == True:
        # Si el juego sigue corriendo y no hay una estrella en la nueva posicion
        # Actualizar mapa
        if game_map[position_columns][position_rows] != star:
            update_game_map(position_columns, position_rows, last_position_columns, last_position_rows)
        else:
            # De lo contrario terminar el juego
            is_game_running = False
            user_wins = False

finilizing_game(user_wins)