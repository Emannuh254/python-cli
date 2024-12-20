from farmers import view_farmers, find_farmer, delete_farmer, add_farmer
from collectors import add_collector, view_collectors, find_collector, delete_collector
from director import add_director, view_directors, find_director, delete_director
from filter import filter_by_name, filter_by_most_milk, filter_by_region
from region import view_regions, find_region, delete_region, generate_sample_regions

# Farmers Menu loop
def farmers_menu():
    while True:
        print("\nFarmers Menu:")
        print("1. View List of Farmers")
        print("2. Add a New Farmer")
        print("3. Find a Farmer by Name")
        print("4. Delete a Farmer by ID")
        print("5. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_farmers()
        elif choice == '2':
            name = input("Enter the farmer's name: ")
            contact = input("Enter the farmer's contact number: ")
            region = input("Enter the farmer's region: ")
            try:
                milk_produced = float(input("Enter the amount of milk produced (in liters): "))
                add_farmer(name, contact, region, milk_produced)
                print("Farmer added successfully.")
            except ValueError:
                print("Invalid input. Please enter a numeric value for milk produced.")
        elif choice == '3':
            name = input("Enter the farmer's name to search: ")
            find_farmer(name)
        elif choice == '4':
            try:
                id = int(input("Enter the ID of the farmer to delete: "))
                delete_farmer(id)
            except ValueError:
                print("Please enter a valid ID.")
        elif choice == '5':
            break  # Return to the main menu
        else:
            print("Invalid choice. Please try again.")

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
                print("Invalid input. Please enter a numeric value for total milk collected.")
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

# Directors Menu loop
def directors_menu():
    while True:
        print("\nDirectors Menu:")
        print("1. View List of Directors")
        print("2. Add a New Director")
        print("3. Find a Director by Name")
        print("4. Delete a Director by ID")
        print("5. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_directors()
        elif choice == '2':
            name = input("Enter the director's name: ")
            contact_number = input("Enter the director's contact number: ")
            region = input("Enter the director's region: ")
            try:
                salary = float(input("Enter the director's salary: "))
                add_director(name, contact_number, region, salary)
                print("Director added successfully!")
            except ValueError:
                print("Invalid input for salary. Please try again.")
        elif choice == '3':
            name = input("Enter the director's name to search: ")
            find_director(name)
        elif choice == '4':
            try:
                id = int(input("Enter the ID of the director to delete: "))
                delete_director(id)
            except ValueError:
                print("Please enter a valid ID.")
        elif choice == '5':
            break  # Return to the main menu
        else:
            print("Invalid choice. Please try again.")

# Filter Menu loop
def filter_menu():
    while True:
        print("\nFilter Menu:")
        print("1. Filter by Name")
        print("2. Filter by Most Milk Collected")
        print("3. Filter by Region")
        print("4. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name to search: ")
            filter_by_name(name)
        elif choice == '2':
            filter_by_most_milk()
        elif choice == '3':
            region_name = input("Enter the region to filter by: ")
            filter_by_region(region_name)
        elif choice == '4':
            break  # Return to the main menu
        else:
            print("Invalid choice. Please try again.")

# Region Menu loop
def region_menu():
    while True:
        print("\nRegion Menu:")
        print("1. View List of Regions")
        print("2. Find a Region by Name")
        print("3. Delete a Region by ID")
        print("4. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_regions()
        elif choice == '2':
            name = input("Enter the region's name to search: ")
            find_region(name)
        elif choice == '3':
            try:
                id = int(input("Enter the ID of the region to delete: "))
                delete_region(id)
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
        print("2. Collectors Menu")
        print("3. Directors Menu")
        print("4. Filter Menu")
        print("5. Region Menu")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            farmers_menu()  # Call the farmers menu
        elif choice == '2':
            collectors_menu()  # Call the collectors menu
        elif choice == '3':
            directors_menu()  # Call the directors menu
        elif choice == '4':
            filter_menu()  # Call the filter menu
        elif choice == '5':
            region_menu()  # Call the region menu
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
