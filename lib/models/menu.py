import curses
from farmers_menu import farmers_menu
from region_menu import region_menu
from filter_menu import filter_menu
from farmers import generate_sample_farmers
from region import generate_sample_regions

# Welcome screen function
def welcome_screen(stdscr):
    # Clear the screen and get screen dimensions
    height, width = stdscr.getmaxyx()
    stdscr.clear()

    # Define the welcome message and description
    welcome_message = "Welcome to the Milk Collection Center!"
    description = "Helping farmers, collectors, and directors streamline milk processes."
    prompt = "Press any key to continue..."
    
    # Display the welcome message, description, and prompt
    stdscr.addstr(height // 2 - 2, (width - len(welcome_message)) // 2, welcome_message)
    stdscr.addstr(height // 2, (width - len(description)) // 2, description)
    stdscr.addstr(height // 2 + 2, (width - len(prompt)) // 2, prompt)

    # Refresh the screen and wait for a key press
    stdscr.refresh()
    stdscr.getch()  # Wait for any key to continue

# Main menu function
def main_menu(stdscr):
    # Generate sample data
    generate_sample_farmers()  # Add sample farmers initially
    generate_sample_regions()  # Add sample regions initially
    
    while True:
        # Clear the screen and get screen dimensions
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        
        # Define the menu options
        stdscr.addstr(height // 2 - 2, (width - len("Main Menu:")) // 2, "Main Menu:")
        stdscr.addstr(height // 2, (width - len("1. Farmers Menu")) // 2, "1. Farmers Menu")
        stdscr.addstr(height // 2 + 1, (width - len("2. Region Menu")) // 2, "2. Region Menu")
        stdscr.addstr(height // 2 + 2, (width - len("3. Filter Menu")) // 2, "3. Filter Menu")
        stdscr.addstr(height // 2 + 3, (width - len("4. Exit")) // 2, "4. Exit")

        stdscr.refresh()

        # Wait for user input
        choice = stdscr.getkey()

        if choice == '1':
            farmers_menu(stdscr)  # Run the farmers menu
        elif choice == '2':
            region_menu(stdscr)  # Run the region menu
        elif choice == '3':
            filter_menu(stdscr)  # Run the filter menu
        elif choice == '4':
            break  # Exit the menu
        else:
            stdscr.addstr(height // 2 + 5, (width - len("Invalid choice. Please try again.")) // 2, "Invalid choice. Please try again.")
            stdscr.refresh()
            stdscr.getch()  # Wait for the user to press any key to continue

# Main function to handle the screen flow
def main(stdscr):
    # Show the welcome screen
    welcome_screen(stdscr)
    
    # Show the main menu after the welcome screen
    main_menu(stdscr)

# Start the application using curses.wrapper
if __name__ == "__main__":
    curses.wrapper(main)
