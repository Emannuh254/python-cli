from director import add_director, view_directors, find_director, delete_director

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

# Test the menu
if __name__ == "__main__":
    directors_menu()
