import random
from all_list import letters
from all_list import numbers
from all_list import symbols
print("Welcome to the Pypassword generator!")

password_letters = int(input("How many letters do you want in your password?: "))
password_symbols = int(input("How many symbols do you want in your password?: "))
password_numbers = int(input("How many numbers do you want in your password?: "))

password_list = []

for letter in range(password_letters):
    password_list += random.choice(letters)

for symbol in range(password_symbols):
    password_list += random.choice(symbols)

for number in range(password_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)
password = ""

for character in password_list:
    password += character

print(f"Your password is: {password}")
