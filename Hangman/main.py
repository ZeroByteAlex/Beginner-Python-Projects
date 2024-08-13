from hangman_ascii_art import title
from hangman_ascii_art import hangman
from word_list import words
import random

print(title)

random_word = random.choice(words)
num_of_blanks = 0
blank_list = []
character_list = []

for letter in random_word:
    num_of_blanks += 1
    blank_list += "_"
    character_list += letter

game_over = False
lives = 6
guessed_letters = []

while not game_over:
    print(f"\nThis word has {num_of_blanks} letters: {blank_list}")

    for life in range(7):
        if lives == 6 - life:
            print(hangman[life])

    print(f"Guesses remaining: {lives}")

    guess = input("What letter do you want to guess?: ").lower()

    if guess not in character_list:
        lives -= 1

    if guess not in guessed_letters:
        guessed_letters.append(guess)
    else:
        print(f"\nYou have already guessed {guess}, try another letter.")
        print(f"Letters guessed: {guessed_letters}")
        if guess not in character_list:
            lives += 1

    for num in range(num_of_blanks):
        if character_list[num] == guess and blank_list[num] == "_":
            blank_list[num] = guess

    if blank_list == character_list:
        print(f"You got the correct word and saved the hangman! YOU WIN!")
        game_over = True
    elif lives == 0:
        print(hangman[6])
        print(f"You ran out of guesses. The word was {random_word}. YOU LOSE!")
        game_over = True
