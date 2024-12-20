# region_menu.py
from region import view_regions, find_region, delete_region, generate_sample_regions

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
