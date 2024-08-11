import random
from rock_paper_scissor_ascii_art import rock
from rock_paper_scissor_ascii_art import paper
from rock_paper_scissor_ascii_art import scissors

print("Welcome to the rock, paper, scissors game!\n")
computer_hand = random.choice(["rock", "paper", "scissors"])

hand = ""
while hand != "rock" and hand != "paper" and hand != "scissors":
    hand = input("Rock, paper, or scissors?: ").lower()

    if hand == "rock":
        print(rock + '\n')

        if computer_hand == "rock":
            print(rock + "\nIt's a tie!")
        elif computer_hand == "paper":
            print(paper + "\nPaper beats rock! You Lose!")
        else:
            print(scissors + "\nRock beats scissors! You Win!")
    elif hand == "paper":
        print(paper + '\n')

        if computer_hand == "rock":
            print(rock + "\nPaper beats rock! You Win!")
        elif computer_hand == "paper":
            print(paper + "\nIt's a tie!")
        else:
            print(scissors + "\nScissors beats paper! You Lose!")
    elif hand == "scissors":
        print(scissors + '\n')

        if computer_hand == "rock":
            print(rock + "\nRock beats scissors! You Lose!")
        elif computer_hand == "paper":
            print(paper + "\nScissors beats paper! You Win!")
        else:
            print(scissors + "\nIt's a tie!")
    else:
        print("Invalid input! Try again.\n")
