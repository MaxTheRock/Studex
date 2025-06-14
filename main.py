from colorama import Fore
import os
import json
import questionary
import time
from programs import dashboard as dash

def typing_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def red(text): typing_print(Fore.RED + text + Fore.RESET)
def yellow(text): typing_print(Fore.YELLOW + text + Fore.RESET)
def green(text): typing_print(Fore.GREEN + text + Fore.RESET)
def cyan(text): typing_print(Fore.CYAN + text + Fore.RESET)
def blue(text): typing_print(Fore.BLUE + text + Fore.RESET)

def clear():
    print("\033[H\033[J", end="")

def school_name_formatter(school_name):
    school_name = school_name.lower()
    words = school_name.split()
    formatted_words = [word if word == "of" else word.capitalize() for word in words]
    return " ".join(formatted_words)

def main():
    clear()
    print("Checking for user info...")
    clear()
    if os.path.exists("data/user_info.json"):
        with open("data/user_info.json", "r") as file:
            dash.main(json.load(file))
    else:
        clear()
        cyan("⭐ Welcome to Studex! Let's set up your profile. ⭐")
        time.sleep(1)
        print()
        forename = input(Fore.YELLOW + "1. Enter your first name: ")
        time.sleep(0.2)
        surname = input(Fore.GREEN + "2. Enter your last name: ")
        time.sleep(0.2)
        age = input(Fore.YELLOW + "3. Enter your age: ")
        time.sleep(0.2)
        school_name = input(Fore.GREEN + "4. Enter your school name: ")
        time.sleep(0.2)
        clear()
        time.sleep(0.5)
        cyan("⭐ Great, let's now select your subjects. ⭐")
        time.sleep(0.5)

        subject_choices = ["Chemistry", "Biology", "Physics", "Maths"]

        subjects = questionary.checkbox(
            "Select all subjects you take:",
            choices=subject_choices
        ).ask()

        with open("data/user_info.json", "w") as file:
            user_data = {
                "forename": forename,
                "surname": surname,
                "age": int(age),
                "school_name": school_name_formatter(school_name),
                "streak": 0,
                "xp": 0,
                "subjects": subjects,
                "progress": {}
            }
            file.write(json.dumps(user_data, indent=2))

        clear()
        green("User info saved successfully!")
        time.sleep(1)
        print()
        green("\n⭐ From now on, every time you run this file, your progress will be saved! ⭐")
        time.sleep(2)
        cyan("\nYou can find your user info in data/user_info.json")
        time.sleep(2)
        print()
        blue(f"\nLet's get started with Studex! And remember {forename}, revision is key to success!")

if __name__ == "__main__":
    main()
    print(Fore.RESET)