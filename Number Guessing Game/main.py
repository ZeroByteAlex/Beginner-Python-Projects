from art import logo
import random


def user_choice():
    decision = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    while decision not in ['easy', 'hard']:
        print("Invalid input, please try again.")
        decision = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if decision == 'easy':
        lives = 10
        return lives
    else:
        lives = 5
        return lives


def player_guessing(num, lives):
    guess_list = []

    while lives != 0:
        print(f"You have {lives} attempts remaining to guess the number.\n")
        print(f"Numbers guessed: {guess_list}")
        guess = int(input("Make a guess: "))

        if guess in guess_list:
            print(f"You already guessed {guess}.")
        elif guess < num:
            guess_list.append(guess)
            print("Too low.")
            lives -= 1
        elif guess > num:
            guess_list.append(guess)
            print("Too high.")
            lives -= 1
        else:
            print(f"You got it! The answer was {num}.")
            break

    if lives == 0:
        print(f"You ran out of guesses. The number was {num}.")


def main():
    print(logo)

    random_number = random.randint(1, 100)

    print("Choose a number between 1 and 100.")

    # Assigning 'guesses_left' to a function called 'user_choice()'
    guesses_left = user_choice()

    # Parameter lines: (42, 47)
    player_guessing(random_number, guesses_left)


if __name__ == "__main__":
    main()
