from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Set up the base class for all models
Base = declarative_base()

# Define the Director model
class Director(Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    contact_number = Column(String(15), nullable=True)
    region = Column(String(50), unique=True, nullable=False)

    # Relationship with Collectors
    collectors = relationship('Collector', back_populates='director', cascade="all, delete-orphan")

    def __init__(self, name, contact_number, region):
        self.name = name
        self.contact_number = contact_number
        self.region = region

    def __repr__(self):
        return f"<Director(name={self.name}, region={self.region})>"

# Define the Collector model
class Collector(Base):
    __tablename__ = 'collectors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    contact_number = Column(String(15), nullable=True)
    region = Column(String(50), nullable=True)
    total_collected = Column(Float, nullable=False)

    # Foreign key to link with Director
    director_id = Column(Integer, ForeignKey('directors.id'), nullable=True)

    # Relationship with Director
    director = relationship('Director', back_populates='collectors')

    def __init__(self, name, contact_number, region, total_collected, director_id=None):
        self.name = name
        self.contact_number = contact_number
        self.region = region
        self.total_collected = total_collected
        self.director_id = director_id

    def __repr__(self):
        return f"<Collector(name={self.name}, region={self.region}, total_collected={self.total_collected})>"

# Create an engine to connect to the database
engine = create_engine('sqlite:///milk_collector.db', echo=True)

# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Function to add a director
def add_director(name, contact_number, region):
    new_director = Director(name=name, contact_number=contact_number, region=region)
    session.add(new_director)
    session.commit()

# Function to view the list of directors
def view_directors():
    directors = session.query(Director).all()
    for director in directors:
        print(f"ID: {director.id} | Name: {director.name} | Region: {director.region}")

# Function to assign collectors to a director
def assign_collectors_to_director(director_id, collector_ids):
    director = session.query(Director).filter(Director.id == director_id).first()
    if director:
        for collector_id in collector_ids:
            collector = session.query(Collector).filter(Collector.id == collector_id).first()
            if collector and collector.region == director.region:
                collector.director_id = director_id
        session.commit()
        print(f"Collectors assigned to Director ID {director_id}.")
    else:
        print(f"Director with ID {director_id} not found.")

# Directors Menu loop
def directors_menu():
    while True:
        print("\nDirectors Menu:")
        print("1. View List of Directors")
        print("2. Add a Director")
        print("3. Assign Collectors to a Director")
        print("4. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_directors()
        elif choice == '2':
            name = input("Enter the director's name: ")
            contact_number = input("Enter the director's contact number: ")
            region = input("Enter the director's region: ")
            add_director(name, contact_number, region)
        elif choice == '3':
            try:
                director_id = int(input("Enter the ID of the director: "))
                collector_ids = input("Enter the IDs of collectors to assign (comma-separated): ").split(',')
                collector_ids = [int(cid.strip()) for cid in collector_ids]
                assign_collectors_to_director(director_id, collector_ids)
            except ValueError:
                print("Please enter valid IDs.")
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
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Farmers Menu (Under Construction)")
        elif choice == '2':
            print("Collectors Menu (Under Construction)")
        elif choice == '3':
            directors_menu()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Main entry point
if __name__ == "__main__":
    main_menu()
