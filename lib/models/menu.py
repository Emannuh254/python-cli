# menu.py (or main.py)
from farmers_menu import farmers_menu
from region_menu import region_menu
from filter_menu import filter_menu  # Importing the filter menu
from farmers import generate_sample_farmers
from region import generate_sample_regions

# Main entry point
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Farmers Menu")
        print("2. Region Menu")
        print("3. Filter Menu")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            farmers_menu()  # Run the farmers menu
        elif choice == '2':
            region_menu()  # Run the region menu
        elif choice == '3':
            filter_menu()  # Run the filter menu
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    generate_sample_farmers()  # Add sample farmers initially
    generate_sample_regions()  # Add sample regions initially
    main_menu()  # Call the main menu function
