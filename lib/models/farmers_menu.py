from farmers import view_farmers, find_farmer, delete_farmer, generate_sample_farmers

# Farmers Menu loop
def farmers_menu():
    while True:
        print("\nFarmers Menu:")
        print("1. View List of Farmers")
        print("2. Find a Farmer by Name")
        print("3. Delete a Farmer by ID")
        print("4. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_farmers()
        elif choice == '2':
            name = input("Enter the farmer's name to search: ")
            find_farmer(name)
        elif choice == '3':
            try:
                id = int(input("Enter the ID of the farmer to delete: "))
                delete_farmer(id)
            except ValueError:
                print("Please enter a valid ID.")
        elif choice == '4':
            break  # Return to the main menu
        else:
            print("Invalid choice. Please try again.")

# Main Menu loop
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Farmers Menu")
        print("2. Collectors Menu")  # Placeholder for future menu
        print("3. Regional Directors Menu")  # Placeholder for future menu
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            farmers_menu()
        elif choice == '2':
            print("Collectors Menu (Under Construction)")
        elif choice == '3':
            print("Regional Directors Menu (Under Construction)")
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
