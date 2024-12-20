# filter.py
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from farmers import Farmer  # Assuming Farmer model is in farmers.py
from region import Region  # Assuming Region model is in region.py (if it's used for region filtering)

# Connect to the database
engine = create_engine('sqlite:///milk_collector.db', echo=True)


Session = sessionmaker(bind=engine)
session = Session()

# Function to filter by name
def filter_by_name(name):
    results = session.query(Farmer).filter(Farmer.name.ilike(f"%{name}%")).all()
    if results:
        for farmer in results:
            print(f"ID: {farmer.id} | Name: {farmer.name} | Region: {farmer.region} | Milk Produced: {farmer.milk_produced}L")
    else:
        print("No farmers found with that name.")

# Function to filter by most milk collected (descending order)
def filter_by_most_milk():
    results = session.query(Farmer).order_by(Farmer.milk_produced.desc()).all()
    if results:
        for farmer in results:
            print(f"ID: {farmer.id} | Name: {farmer.name} | Region: {farmer.region} | Milk Produced: {farmer.milk_produced}L")
    else:
        print("No farmers found.")

# Function to filter by region
def filter_by_region(region_name):
    results = session.query(Farmer).filter(Farmer.region.ilike(f"%{region_name}%")).all()
    if results:
        for farmer in results:
            print(f"ID: {farmer.id} | Name: {farmer.name} | Region: {farmer.region} | Milk Produced: {farmer.milk_produced}L")
    else:
        print(f"No farmers found in the region '{region_name}'.")
