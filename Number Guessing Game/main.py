import random

print("Welcome to the random number guessing game!\n")

lives = 0
difficulty = input("Choose your difficulty: Easy (7 guesses), Medium (5 guesses),"
                   " Hard (3 guesses), or Lucky (1 guess)\n").lower()

while difficulty not in ["easy", "medium", "hard", "lucky"]:
    print("Invalid input! Please enter 'easy', 'medium', 'hard', or 'lucky'\n")
    difficulty = input("Choose your difficulty: Easy (7 guesses), Medium (5 guesses),"
                       " Hard (3 guesses), Lucky (1 guess)\n").lower()

if difficulty == "easy":
    lives = 7
elif difficulty == "medium":
    lives = 5
elif difficulty == "hard":
    lives = 3
else:
    lives = 1

if lives > 1:
    print(f"You have {lives} guesses.")
else:
    print(f"You have {lives} guess.")

random_number_output = random.randint(1, 15)
random_number_guess = random.randint(1, random_number_output)
random_guess = int(input(f"Guess a number between 1 - {random_number_output}: "))

while lives != 0:
    if random_guess != random_number_guess:
        lives -= 1
        if lives == 0:
            print("You ran out of guesses, YOU LOSE.")
            break
        print(f"Sorry, that is not the correct number. You have {lives} guesses left.")
        random_guess = int(input(f"Guess a number between 1 - {random_number_output}: "))
    elif random_guess == random_number_guess:
        print("Congrats! You guessed the correct number, YOU WIN!")
        break
    else:
        print("Unknown error occurred!")
        break
