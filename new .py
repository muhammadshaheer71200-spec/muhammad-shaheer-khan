import random

def play():
    user = input("Enter your choice (rock, paper, or scissor): ").lower()
    computer = random.choice(['rock', 'paper', 'scissor'])

    print("You chose:", user, " Computer chose:", computer)

    if user == computer:
        print("It's a draw!")

    elif user == "rock":
        if computer == "scissor":
            print("You win!")
        else:
            print("You lose!")

    elif user == "paper":
        if computer == "rock":
            print("You win!")
        else:
            print("You lose!")

    elif user == "scissor":
        if computer == "paper":
            print("You win!")
        else:
            print("You lose!")
    else:
        print("Invalid input, please choose rock, paper, or scissor.")
play()




