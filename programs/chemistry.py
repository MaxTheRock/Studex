from colorama import Fore, Style
import time
import random
import shutil
import json
import questionary


def printProgressBar(
    iteration,
    total,
    prefix="",
    suffix="",
    usepercent=True,
    decimals=1,
    fill=Style.BRIGHT + Fore.CYAN + "-" + Style.RESET_ALL,
):
    twx, _ = shutil.get_terminal_size()
    length = twx - 1 - len(prefix) - len(suffix) - 4
    if usepercent:
        length -= 2
    filledLength = int(length * iteration // total)
    length = max(0, length - 10)
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + Fore.BLACK + "-" * (length - filledLength)
    if usepercent:
        percent = ("{0:." + str(decimals) + "f}").format(
            100 * (iteration / float(total))
        )
        print(
            "\r    %s |%s| %s/%s" % (prefix, bar, Fore.RESET + str(iteration), total),
            end="",
            flush=True,
        )
    else:
        print("\r%s |%s| %s" % (prefix, bar, suffix), end="", flush=True)
    if iteration == total:
        print(flush=True)


def typing_print(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)


def red(text):
    typing_print(Fore.RED + text + Fore.RESET)


def yellow(text):
    typing_print(Fore.YELLOW + text + Fore.RESET)


def green(text):
    typing_print(Fore.GREEN + text + Fore.RESET)


def cyan(text):
    typing_print(Fore.CYAN + text + Fore.RESET)


def blue(text):
    typing_print(Fore.BLUE + text + Fore.RESET)


def clear():
    print("\033[H\033[J", end="")


def menu(title, list):
    global choice
    choice = questionary.select(title, choices=list).ask()


def main():
    with open("data/chemistry.json", "r") as file:
        chem_info = json.load(file)
    with open("data/user_info.json", "r") as file2:
        user_info = json.load(file2)
    clear()
    xp = user_info.get("xp", 0)
    if not isinstance(xp, int) or not (0 <= xp <= 100):
        raise ValueError("user_info.json 'xp' must be an integer between 0 and 100")

    printProgressBar(xp, 100, prefix="Total XP", suffix="", usepercent=True)
    print("\n")
    menu("Select a topic", (chem_info.get("topics", [])))
    
