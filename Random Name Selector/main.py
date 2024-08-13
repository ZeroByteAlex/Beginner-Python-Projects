import random
from title_ascii_art import title

print(title)

exiting_program = False
name_list = []
random_name = ""

while not exiting_program:
    user_input = input("Enter a name: ")
    name_list.append(user_input)

    selector = {
        "name": name_list
    }

    names = ", ".join(name_list)
    print(f"\nHere is a list of the names saved: {names}\n")

    exit_program = input("Do you want to enter another name before the selector is activated (y/n)?: ").lower()

    if exit_program == "yes" or exit_program == "y":
        exiting_program = False
    elif exit_program == "no" or exit_program == "n":
        exiting_program = True
        random_name = random.choice(selector["name"])
    else:
        while exit_program not in ["yes", "y", "no", "n"]:
            print("Please enter 'y' or 'n' to continue.\n")
            exit_program = input("Do you want to enter another name before the selector is activated (y/n)?: ").lower()
            if exit_program == "yes" or exit_program == "y":
                exiting_program = False
            elif exit_program == "no" or exit_program == "n":
                exiting_program = True
                random_name = random.choice(selector["name"])

print(f"The random name that was chosen is: {random_name}")
