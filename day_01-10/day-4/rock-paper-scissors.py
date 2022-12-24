
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#Write your code below this line 👇

import random

game_options = [rock, paper, scissors]

user_input = int(input("Select an option:\n0-rock\n1-paper\n2-scissors\n---> "))
computer_input = random.randint(0,2)

if user_input >= 0 and user_input <= 2:

    user_selection = game_options[user_input]
    computer_selection = game_options[computer_input]

    print(user_selection)
    print(computer_selection)

    if user_input == 0 and computer_input == 1:
        # If the user selected rock and the computer paper
        print("\nComputer WINS\n")
    elif user_input == 0 and computer_input == 2:
        # If the user selected rock and the computer scissor
        print("\nYOU WIN!!!\n")
    elif user_input == 1 and computer_input == 0:
        # If the user selected paper and the computer rock
        print("\nYOU WIN!!!\n")
    elif user_input == 1 and computer_input == 2:
        # If the user selected paper and the computer scissor
        print("\nComputer WINS\n")
    elif user_input == 2 and computer_input == 0:
        # if the user selects scissors and computer selects rock
        print("\nYOU WIN!!!\n")
    elif user_input == 2 and computer_input == 1:
        # If the user selects scissors and computer selects paper
        print("\nComputer WINS\n")
    else:
        print("It's a tie")

else:
    print("Wrong entry!")





