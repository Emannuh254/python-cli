from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up the base class for all models
Base = declarative_base()

# Define the Farmers model
class Farmer(Base):
    __tablename__ = 'farmers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    contact_number = Column(String(15), nullable=True)
    region = Column(String(50), nullable=True)
    milk_produced = Column(Float, nullable=False)

    def __init__(self, name, contact_number, region, milk_produced):
        self.name = name
        self.contact_number = contact_number
        self.region = region
        self.milk_produced = milk_produced

    def __repr__(self):
        return f"<Farmer(name={self.name}, region={self.region}, milk_produced={self.milk_produced})>"

# Create an engine to connect to the database (SQLite in this case)
engine = create_engine('sqlite:///milk_collector.db', echo=True)

# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Function to add a farmer
def add_farmer(name, contact_number, region, milk_produced):
    new_farmer = Farmer(name=name, contact_number=contact_number, region=region, milk_produced=milk_produced)
    session.add(new_farmer)
    session.commit()

# Function to generate 20 sample farmers
def generate_sample_farmers():
    sample_farmers = [
        ('John Doe', '1234567890', 'Central Region', 150.0),
        ('Jane Smith', '2345678901', 'North Region', 120.5),
        ('Alice Johnson', '3456789012', 'South Region', 100.2),
        ('Bob Brown', '4567890123', 'West Region', 200.3),
        ('Charlie White', '5678901234', 'East Region', 180.7),
        ('David Black', '6789012345', 'Central Region', 130.0),
        ('Eve Green', '7890123456', 'North Region', 170.0),
        ('Frank Gray', '8901234567', 'South Region', 110.5),
        ('Grace Blue', '9012345678', 'West Region', 140.5),
        ('Hannah Red', '0123456789', 'East Region', 160.0),
        ('Ivan Yellow', '1234509876', 'Central Region', 145.0),
        ('Jack Purple', '2345610987', 'North Region', 155.5),
        ('Kathy Pink', '3456721098', 'South Region', 95.0),
        ('Leo Orange', '4567832109', 'West Region', 110.0),
        ('Mona Violet', '5678943210', 'East Region', 120.5),
        ('Nina Brown', '6789054321', 'Central Region', 160.0),
        ('Oscar Silver', '7890165432', 'North Region', 135.0),
        ('Paul Gold', '8901276543', 'South Region', 125.0),
        ('Quincy Copper', '9012387654', 'West Region', 150.5),
        ('Rachel Bronze', '0123498765', 'East Region', 180.5)
    ]

    # Add each sample farmer to the database
    for farmer in sample_farmers:
        add_farmer(*farmer)

# Function to view the list of farmers
def view_farmers():
    farmers = session.query(Farmer).all()
    for farmer in farmers:
        print(f"ID: {farmer.id} | Name: {farmer.name} | Region: {farmer.region} | Milk Produced: {farmer.milk_produced}L")

# Function to find a farmer by name
def find_farmer(name):
    farmer = session.query(Farmer).filter(Farmer.name.ilike(f'%{name}%')).all()
    if farmer:
        for f in farmer:
            print(f"ID: {f.id} | Name: {f.name} | Region: {f.region} | Milk Produced: {f.milk_produced}L")
    else:
        print("Farmer not found.")

# Function to delete a farmer by ID
def delete_farmer(id):
    farmer_to_delete = session.query(Farmer).filter(Farmer.id == id).first()
    if farmer_to_delete:
        session.delete(farmer_to_delete)
        session.commit()
        print(f"Farmer with ID {id} deleted successfully.")
    else:
        print(f"Farmer with ID {id} not found.")
