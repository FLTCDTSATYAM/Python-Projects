### Rock-Paper-Scissor Game ###

# Algorithm
'''  
1. Input from user as rock, paper or scissor
2. Computer will randomly generate it's output from three
3. Wirte logic of it that who will win
4. Display result

# ----------logic----------#
case 1: Rock
Rock - Rock = Tie
Rock - Paper = Paper (wins)
Rock - Scissor = Rock (wins)

case 2: Paper
Paper - Paper = Tie
Paper - Rock = Paper (wins)
Paper - Scissor = Scissor (wins)

case 3: Scissor
Scissor - Scissor = Tie
Scissor - Rock = Rock (wins)
Scissor - Paper = Scissor (wins)

# --------------------------------- #
'''
import random
#user choice
userName = input("Enter your name to start the game: ")
user_turn = input("Enter your choice (Rock, Paper, Scissor): ")
#computer choice
choice = ["Rock", "Paper", "Scissor"]
computer_turn = random.choice(choice)

if(user_turn == "Rock"):
    if(computer_turn == "Rock"):
        print(f"{userName} choice = {user_turn}, Computer choice = {computer_turn}")
        print("\033[1;34mIt's a tie\033[0m")
    elif(computer_turn == "Paper"):
        print(f"{userName} choice = {user_turn}, Computer choice = {computer_turn}")
        print("\033[1;34mComputer wins\033[0m")
    else:
        print(f"{userName} choice = {user_turn}, Computer choice = {computer_turn}")
        print(f"\033[1;34m{userName} wins\033[0m")
elif(user_turn == "Paper"):
    if(computer_turn == "Rock"):
        print(f"{userName} choice = {user_turn}, Computer choice = {computer_turn}")
        print(f"\033[1;34m{userName} wins\033[0m")
    elif(computer_turn == "Paper"):
        print(f"{userName} choice = {user_turn}, Computer choice = {computer_turn}")
        print("\033[1;34mIt's a tie\033[0m")
    else:
        print(f"{userName} choice = {user_turn}, Computer choice = {computer_turn}")
        print("\033[1;34mComputer wins\033[0m")
elif(user_turn == "Scissor"):
    if(computer_turn == "Rock"):
        print(f"{userName} choice = {user_turn}, Computer choice = {computer_turn}")
        print("\033[1;34mComputer wins\033[0m")
    elif(computer_turn == "Paper"):
        print(f"{userName} choice = {user_turn}, Computer choice = {computer_turn}")
        print(f"\033[1;34m{userName} wins\033[0m")
    else:
        print(f"{userName} choice = {user_turn}, Computer choice = {computer_turn}")
        print("\033[1;34mIt's a tie\033[0m")
else:
    print("\033[1mEnter a valid Input\033[0m")



