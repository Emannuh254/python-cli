from collectors import add_collector, view_collectors, find_collector, delete_collector

# Collectors Menu loop
def collectors_menu():
    while True:
        print("\nCollectors Menu:")
        print("1. View List of Collectors")
        print("2. Add a New Collector")
        print("3. Find a Collector by Name")
        print("4. Delete a Collector by ID")
        print("5. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_collectors()
        elif choice == '2':
            name = input("Enter the collector's name: ")
            contact = input("Enter the collector's contact number: ")
            region = input("Enter the collector's region: ")
            try:
                total = float(input("Enter the total milk collected (in liters): "))
                add_collector(name, contact, region, total)
                print("Collector added successfully.")
            except ValueError:
                print("Invalid input. Please enter numeric value for total milk collected.")
        elif choice == '3':
            name = input("Enter the collector's name to search: ")
            find_collector(name)
        elif choice == '4':
            try:
                id = int(input("Enter the ID of the collector to delete: "))
                delete_collector(id)
            except ValueError:
                print("Please enter a valid ID.")
        elif choice == '5':
            break  # Return to the main menu
        else:
            print("Invalid choice. Please try again.")

# Main Menu loop
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Farmers Menu")
        print("2. Collectors Menu")
        print("3. Regional Directors Menu")  # Placeholder for future menu
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            farmers_menu()  # Assuming you have a farmers_menu function defined elsewhere
        elif choice == '2':
            collectors_menu()  # Call the collectors menu
        elif choice == '3':
            print("Regional Directors Menu (Under Construction)")  # Placeholder
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
