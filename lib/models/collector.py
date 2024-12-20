from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up the base class for all models
Base = declarative_base()

# Define the Collectors model
class Collector(Base):
    __tablename__ = 'collectors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    contact_number = Column(String(15), nullable=True)
    region = Column(String(50), nullable=True)
    total_collected = Column(Float, nullable=False)

    def __init__(self, name, contact_number, region, total_collected):
        self.name = name
        self.contact_number = contact_number
        self.region = region
        self.total_collected = total_collected

    def __repr__(self):
        return f"<Collector(name={self.name}, region={self.region}, total_collected={self.total_collected})>"

# Create an engine to connect to the database
engine = create_engine('sqlite:///milk_collector.db', echo=True)

# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Function to add a collector
def add_collector(name, contact_number, region, total_collected):
    new_collector = Collector(name=name, contact_number=contact_number, region=region, total_collected=total_collected)
    session.add(new_collector)
    session.commit()

# Function to generate 20 sample collectors
def generate_sample_collectors():
    sample_collectors = [
        ('Alice Smith', '1234567890', 'Central Region', 500.0),
        ('Bob Johnson', '2345678901', 'North Region', 420.5),
        ('Charlie Brown', '3456789012', 'South Region', 380.2),
        ('David Williams', '4567890123', 'West Region', 600.3),
        ('Eve Davis', '5678901234', 'East Region', 450.7),
        ('Frank Moore', '6789012345', 'Central Region', 400.0),
        ('Grace Taylor', '7890123456', 'North Region', 490.0),
        ('Hannah Anderson', '8901234567', 'South Region', 310.5),
        ('Ian Thomas', '9012345678', 'West Region', 540.5),
        ('Judy Martin', '0123456789', 'East Region', 480.0),
        ('Kevin White', '1234509876', 'Central Region', 505.0),
        ('Laura Harris', '2345610987', 'North Region', 455.5),
        ('Mark Thompson', '3456721098', 'South Region', 390.0),
        ('Nina Walker', '4567832109', 'West Region', 410.0),
        ('Oscar Scott', '5678943210', 'East Region', 430.5),
        ('Paula Lewis', '6789054321', 'Central Region', 460.0),
        ('Quinn Young', '7890165432', 'North Region', 435.0),
        ('Rachel Allen', '8901276543', 'South Region', 375.0),
        ('Steve Hall', '9012387654', 'West Region', 520.5),
        ('Tina King', '0123498765', 'East Region', 490.5)
    ]

    # Add each sample collector to the database
    for collector in sample_collectors:
        add_collector(*collector)

# Function to view the list of collectors
def view_collectors():
    collectors = session.query(Collector).all()
    for collector in collectors:
        print(f"ID: {collector.id} | Name: {collector.name} | Region: {collector.region} | Total Collected: {collector.total_collected}L")

# Function to find a collector by name
def find_collector(name):
    collector = session.query(Collector).filter(Collector.name.ilike(f'%{name}%')).all()
    if collector:
        for c in collector:
            print(f"ID: {c.id} | Name: {c.name} | Region: {c.region} | Total Collected: {c.total_collected}L")
    else:
        print("Collector not found.")

# Function to delete a collector by ID
def delete_collector(id):
    collector_to_delete = session.query(Collector).filter(Collector.id == id).first()
    if collector_to_delete:
        session.delete(collector_to_delete)
        session.commit()
        print(f"Collector with ID {id} deleted successfully.")
    else:
        print(f"Collector with ID {id} not found.")

# Collectors Menu loop
def collectors_menu():
    while True:
        print("\nCollectors Menu:")
        print("1. View List of Collectors")
        print("2. Find a Collector by Name")
        print("3. Delete a Collector by ID")
        print("4. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_collectors()
        elif choice == '2':
            name = input("Enter the collector's name to search: ")
            find_collector(name)
        elif choice == '3':
            try:
                id = int(input("Enter the ID of the collector to delete: "))
                delete_collector(id)
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
        print("3. Regional Directors Menu")  # Placeholder for future menu
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Farmers Menu (Under Construction)")
        elif choice == '2':
            collectors_menu()
        elif choice == '3':
            print("Regional Directors Menu (Under Construction)")
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Main entry point
if __name__ == "__main__":
    generate_sample_collectors()  # Add sample collectors initially
    main_menu()
