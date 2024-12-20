from filter_menu import filter_menu  # Import filter menu

# Main Menu loop
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Farmers Menu")
        print("2. Collectors Menu")
        print("3. Directors Menu")
        print("4. Filter Menu")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            farmers_menu()  # Call the farmers menu
        elif choice == '2':
            print("Collectors Menu (Under Construction)")
        elif choice == '3':
            directors_menu()  # Call the directors menu
        elif choice == '4':
            filter_menu()  # Call the filter menu
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please try again.")
