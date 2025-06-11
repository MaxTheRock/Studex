from colorama import Fore, Style
import time
import random
import shutil
import json
import curses

menu = ['Option 1', 'Option 2', 'Option 3', 'Exit']
user_data = {}

def print_menu(stdscr, selected_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == selected_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x - 2, f"> {row}")
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def printProgressBar(iteration, total, prefix='', suffix='', usepercent=True, decimals=1, fill=Style.BRIGHT + Fore.CYAN + '-' + Style.RESET_ALL):
    twx, _ = shutil.get_terminal_size()
    length = twx - 1 - len(prefix) - len(suffix) - 4
    if usepercent:
        length -= 2
    length = max(0, length - 10)
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + Fore.BLACK + '-' * (length - filledLength)
    if usepercent:
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        print(f'\r    {prefix} |{bar}| {Fore.RESET}{iteration}/{total}', end='', flush=True)
    else:
        print(f'\r{prefix} |{bar}| {suffix}', end='', flush=True)
    if iteration == total:
        print(flush=True)

def typing_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def red(text): print(Fore.RED + text + Fore.RESET)
def yellow(text): print(Fore.YELLOW + text + Fore.RESET)
def green(text): print(Fore.GREEN + text + Fore.RESET)
def cyan(text): print(Fore.CYAN + text + Fore.RESET)
def blue(text): print(Fore.BLUE + text + Fore.RESET)

def clear(): print("\033[H\033[J", end="")

def pre_curses_intro(data):
    global user_data
    user_data = data
    with open('data/prompts.json', 'r') as f:
        prompts = json.load(f)
    xp = data.get('xp', 0)
    if not isinstance(xp, int) or not (0 <= xp <= 100):
        raise ValueError("user_info.json 'xp' must be an integer between 0 and 100")

    printProgressBar(xp, 100, prefix='Total XP', usepercent=True)
    print()
    cyan(f"\n⭐  {random.choice(prompts.get('greetings'))}, {data['forename']}! ⭐")
    input("\nPress Enter to open the menu...")

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
    current_idx = 0

    while True:
        print_menu(stdscr, current_idx)
        key = stdscr.getch()
        if key == curses.KEY_UP and current_idx > 0:
            current_idx -= 1
        elif key == curses.KEY_DOWN and current_idx < len(menu) - 1:
            current_idx += 1
        elif key in [curses.KEY_ENTER, ord('\n')]:
            if menu[current_idx] == 'Exit':
                break
            stdscr.clear()
            stdscr.addstr(0, 0, f"You selected '{menu[current_idx]}'!")
            stdscr.addstr(2, 0, "Press any key to return to the menu.")
            stdscr.refresh()
            stdscr.getch()
