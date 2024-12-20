import json

# Load data from db.json
def load_data():
    with open('db.json', 'r') as file:
        return json.load(file)

# Helper function to print farmers
def display_farmers(farmers):
    print("\nFarmers List:")
    for farmer in farmers:
        print(f"ID: {farmer['id']}, Name: {farmer['name']}, Region: {farmer['region']}, Milk Produced: {farmer['milk_produced']}L")

# Helper function to find a farmer by name
def find_farmer(farmers, name):
    found_farmers = [farmer for farmer in farmers if name.lower() in farmer['name'].lower()]
    if found_farmers:
        display_farmers(found_farmers)
    else:
        print(f"No farmers found with the name '{name}'.")

# Helper function to delete a farmer by ID
def delete_farmer(farmers, farmer_id):
    farmers = [farmer for farmer in farmers if farmer['id'] != farmer_id]
    return farmers

def farmers_menu():
    data = load_data()
    farmers = data['farmers']
    while True:
        print("\nFarmers Menu:")
        print("1. View List of Farmers")
        print("2. Find a Farmer by Name")
        print("3. Delete a Farmer by ID")
        print("4. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_farmers(farmers)
        elif choice == '2':
            name = input("Enter the farmer's name to search: ")
            find_farmer(farmers, name)
        elif choice == '3':
            try:
                id = int(input("Enter the ID of the farmer to delete: "))
                farmers = delete_farmer(farmers, id)
                print(f"Farmer with ID {id} has been deleted.")
            except ValueError:
                print("Please enter a valid ID.")
        elif choice == '4':
            break  # Return to the main menu
        else:
            print("Invalid choice. Please try again.")

def collectors_menu():
    data = load_data()
    collectors = data['collectors']
    while True:
        print("\nCollectors Menu:")
        print("1. View List of Collectors")
        print("2. Find a Collector by Name")
        print("3. Delete a Collector by ID")
        print("4. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_farmers(collectors)
        elif choice == '2':
            name = input("Enter the collector's name to search: ")
            find_farmer(collectors, name)  # Same function as farmers, can be separated if needed
        elif choice == '3':
            try:
                id = int(input("Enter the ID of the collector to delete: "))
                collectors = delete_farmer(collectors, id)  # Same delete function as farmers
                print(f"Collector with ID {id} has been deleted.")
            except ValueError:
                print("Please enter a valid ID.")
        elif choice == '4':
            break  # Return to the main menu
        else:
            print("Invalid choice. Please try again.")

def regional_directors_menu():
    data = load_data()
    directors = data['regional_directors']
    while True:
        print("\nRegional Directors Menu:")
        print("1. View List of Directors")
        print("2. Find a Director by Name")
        print("3. Delete a Director by ID")
        print("4. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_farmers(directors)
        elif choice == '2':
            name = input("Enter the director's name to search: ")
            find_farmer(directors, name)  # Same function as farmers, can be separated if needed
        elif choice == '3':
            try:
                id = int(input("Enter the ID of the director to delete: "))
                directors = delete_farmer(directors, id)  # Same delete function as farmers
                print(f"Director with ID {id} has been deleted.")
            except ValueError:
                print("Please enter a valid ID.")
        elif choice == '4':
            break  # Return to the main menu
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Farmers Menu")
        print("2. Collectors Menu")
        print("3. Regional Directors Menu")
        print("4. Best Performers")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            farmers_menu()
        elif choice == '2':
            collectors_menu()
        elif choice == '3':
            regional_directors_menu()
        elif choice == '4':
            # Best Performers can be implemented similarly
            print("Best Performers Menu Coming Soon!")
            input("\nPress Enter to return to the main menu.")
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
