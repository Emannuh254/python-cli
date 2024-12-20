import time
from lib.models.menu import main_menu  

def splash_screen():
    print("=" * 50)
    print(" " * 15 + "Welcome to")
    print(" " * 10 + "Milk Collector System")
    print(" " * 7 + "Streamlining Milk Collection for Farmers")
    print("=" * 50)
    time.sleep(2)  # Pause for 2 seconds for effect

if __name__ == "__main__":
    splash_screen()  # Display the splash screen
    main_menu()  # Start the main navigation menu
