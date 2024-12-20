# main.py
import curses
from models.farmers import farmers_menu  # Importing the farmers menu

def welcome_screen(stdscr):
    height, width = stdscr.getmaxyx()
    stdscr.clear()

    welcome_message = "Welcome to the Milk Collection Center!"
    description = "Helping farmers, collectors, and directors streamline milk processes."
    prompt = "Press any key to continue..."
    
    stdscr.addstr(height // 2 - 2, (width - len(welcome_message)) // 2, welcome_message)
    stdscr.addstr(height // 2, (width - len(description)) // 2, description)
    stdscr.addstr(height // 2 + 2, (width - len(prompt)) // 2, prompt)

    stdscr.refresh()
    stdscr.getch()

def main_menu(stdscr):
    options = [
        "1. Farmers",
        "2. Collectors",
        "3. Regional Directors",
        "4. Regions",
        "5. Best Performers",
        "6. Exit"
    ]
    current_selection = 0

    curses.mousemask(curses.ALL_MOUSE_EVENTS)

    while True:
        height, width = stdscr.getmaxyx()
        stdscr.clear()

        title = "Main Menu"
        subtitle = "Use arrow keys to navigate, Enter to select, or click to select."
        stdscr.addstr(2, (width - len(title)) // 2, title, curses.A_BOLD)
        stdscr.addstr(3, (width - len(subtitle)) // 2, subtitle)

        for idx, option in enumerate(options):
            x = (width - len(option)) // 2
            y = 5 + idx
            if idx == current_selection:
                stdscr.addstr(y, x, option, curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, option)

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_selection > 0:
            current_selection -= 1
        elif key == curses.KEY_DOWN and current_selection < len(options) - 1:
            current_selection += 1
        elif key == 10:  # Enter key
            if current_selection == 0:  # Farmers
                farmers_menu(stdscr)  # Call the farmers menu from farmers.py
            elif current_selection == 1:  # Collectors
                pass  # Implement similarly
            elif current_selection == 2:  # Regional Directors
                pass  # Implement similarly
            elif current_selection == 3:  # Regions
                pass  # Implement similarly
            elif current_selection == 4:  # Best Performers
                pass  # Implement similarly
            elif current_selection == 5:  # Exit
                stdscr.clear()
                goodbye_message = "Exiting... Goodbye!"
                stdscr.addstr(height // 2, (width - len(goodbye_message)) // 2, goodbye_message)
                stdscr.refresh()
                stdscr.getch()
                break

def main(stdscr):
    welcome_screen(stdscr)
    main_menu(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
