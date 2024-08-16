from art import logo
import random


def game_start():
    """Makes the game start from the beginning of the program."""
    play_or_not = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()

    if play_or_not == 'y':
        player_choice = True
        return player_choice
    else:
        player_choice = False
        return player_choice


print(logo)

game_running = game_start()

print("")

while game_running:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    hands = {
        "player": random.sample(cards, 2),
        "computer": random.sample(cards, 2)
    }

    hands_num = {
        "player": 0,
        "computer": 0
    }

    def score(player_score, computer_score):
        while computer_score < 17:
            hands["computer"].append(random.choice(cards))
            computer_score = 0
            for dealer_card in hands["computer"]:
                computer_score += dealer_card
        if player_score < computer_score or player_score > 21:
            print(f"\nYour final hand: {hands["player"]}, final score: {hands_num["player"]}")
            print(f"Computer's final hand: {hands["computer"]}, final score: {computer_score}")
            if computer_score > 21 and player_score > 21:
                print("YOU LOSE!")
            elif computer_score > 21:
                print("YOU WIN!")
            else:
                print("YOU LOSE!")
        elif player_score > computer_score or computer_score > 21:
            print(f"\nYour final hand: {hands["player"]}, final score: {hands_num["player"]}")
            print(f"Computer's final hand: {hands["computer"]}, final score: {computer_score}")
            print("YOU WIN!")


    for player_card in hands["player"]:
        hands_num["player"] += player_card

    for computer_card in hands["computer"]:
        hands_num["computer"] += computer_card

    print(f"Your cards: {hands["player"]}, current score: {hands_num["player"]}")
    print(f"Computer's first card: {hands["computer"][0]}")

    end_choice = False
    while not end_choice:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if another_card == 'y':
            hands["player"].append(random.choice(cards))
            hands_num["player"] = 0
            for player_card in hands["player"]:
                hands_num["player"] += player_card
            print(f"Your cards: {hands["player"]}, current score: {hands_num["player"]}")
            print(f"Computer's first card: {hands["computer"][0]}")
        else:
            end_choice = True

        if hands_num["player"] > 21:
            end_choice = True

    score(hands_num["player"], hands_num["computer"])

    game_running = False
