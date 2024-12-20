# filter_menu.py
from filter import filter_by_name, filter_by_most_milk, filter_by_region

# Menu for filtering
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
