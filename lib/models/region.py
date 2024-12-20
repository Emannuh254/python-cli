# region.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up the base class for all models
Base = declarative_base()

# Define the Region model
class Region(Base):
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Region(name={self.name})>"

# Create an engine to connect to the database (SQLite in this case)
engine = create_engine('sqlite:///milk_collector.db', echo=True)

# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Function to add a region
def add_region(name):
    new_region = Region(name=name)
    session.add(new_region)
    session.commit()

# Function to generate some sample regions
def generate_sample_regions():
    sample_regions = ['Central Region', 'North Region', 'South Region', 'West Region', 'East Region']
    for region in sample_regions:
        add_region(region)

# Function to view the list of regions
def view_regions():
    regions = session.query(Region).all()
    for region in regions:
        print(f"ID: {region.id} | Name: {region.name}")

# Function to find a region by name
def find_region(name):
    region = session.query(Region).filter(Region.name.ilike(f'%{name}%')).all()
    if region:
        for r in region:
            print(f"ID: {r.id} | Name: {r.name}")
    else:
        print("Region not found.")

# Function to delete a region by ID
def delete_region(id):
    region_to_delete = session.query(Region).filter(Region.id == id).first()
    if region_to_delete:
        session.delete(region_to_delete)
        session.commit()
        print(f"Region with ID {id} deleted successfully.")
    else:
        print(f"Region with ID {id} not found.")
