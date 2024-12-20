from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up the base class for all models
Base = declarative_base()

# Define the Directors model
class Director(Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    contact_number = Column(String(15), nullable=True)
    region = Column(String(50), nullable=True)
    salary = Column(Float, nullable=False)

    def __init__(self, name, contact_number, region, salary):
        self.name = name
        self.contact_number = contact_number
        self.region = region
        self.salary = salary

    def __repr__(self):
        return f"<Director(name={self.name}, region={self.region}, salary={self.salary})>"

# Create an engine to connect to the database (SQLite in this case)
engine = create_engine('sqlite:///milk_collector.db', echo=True)

# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Function to add a director
def add_director(name, contact_number, region, salary):
    new_director = Director(name=name, contact_number=contact_number, region=region, salary=salary)
    session.add(new_director)
    session.commit()

# Function to generate sample directors
def generate_sample_directors():
    sample_directors = [
        ('Alice Blue', '1112223333', 'North Region', 75000.0),
        ('Bob Green', '2223334444', 'South Region', 68000.0),
        ('Charlie Red', '3334445555', 'West Region', 72000.0),
        ('Diana Yellow', '4445556666', 'East Region', 70000.0),
        ('Evan White', '5556667777', 'Central Region', 78000.0)
    ]

    # Add each sample director to the database
    for director in sample_directors:
        add_director(*director)

# Function to view the list of directors
def view_directors():
    directors = session.query(Director).all()
    for director in directors:
        print(f"ID: {director.id} | Name: {director.name} | Region: {director.region} | Salary: ${director.salary}")

# Function to find a director by name
def find_director(name):
    directors = session.query(Director).filter(Director.name.ilike(f'%{name}%')).all()
    if directors:
        for d in directors:
            print(f"ID: {d.id} | Name: {d.name} | Region: {d.region} | Salary: ${d.salary}")
    else:
        print("Director not found.")

# Function to delete a director by ID
def delete_director(id):
    director_to_delete = session.query(Director).filter(Director.id == id).first()
    if director_to_delete:
        session.delete(director_to_delete)
        session.commit()
        print(f"Director with ID {id} deleted successfully.")
    else:
        print(f"Director with ID {id} not found.")

# Main script for testing
if __name__ == "__main__":
    generate_sample_directors()  # Add sample directors initially
    print("Sample directors added to the database.")
    print("View all directors:")
    view_directors()
