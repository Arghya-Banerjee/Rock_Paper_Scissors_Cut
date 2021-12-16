import random

user_wins = 0
computer_wins = 0
draw_count = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Draw!!")
        draw_count += 1

    elif user_input == "rock" and computer_pick == "rock":
        print("Draw!!")
        draw_count += 1

    elif user_input == "paper" and computer_pick == "paper":
        print("Draw!!")
        draw_count += 1

    elif computer_pick == "rock" and user_input == "scissors":
        print("You Lost!")
        user_wins += 1

    elif computer_pick == "paper" and user_input == "rock":
        print("You Lost!")
        user_wins += 1

    elif computer_pick == "scissors" and user_input == "paper":
        print("You Lost!")
        user_wins += 1

    else:
        None

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Thanks for Playing, Goodbye!")
