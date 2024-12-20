import random
from collectors import add_collector

# Function to generate random names
def generate_random_name():
    first_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ian", "Judy", "Kevin", "Laura", "Mark", "Nina", "Oscar", "Paula", "Quinn", "Rachel", "Steve", "Tina"]
    last_names = ["Smith", "Johnson", "Brown", "Williams", "Davis", "Moore", "Taylor", "Anderson", "Thomas", "Martin", "White", "Harris", "Thompson", "Walker", "Scott", "Lewis", "Young", "Allen", "Hall", "King"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to generate random phone numbers
def generate_random_phone():
    return f"{random.randint(1000000000, 9999999999)}"

# Function to generate random regions
def generate_random_region():
    regions = ["Central Region", "North Region", "South Region", "East Region", "West Region"]
    return random.choice(regions)

# Function to generate random total collected
def generate_random_total_collected():
    return round(random.uniform(100.0, 1000.0), 2)  # Random float between 100 and 1000, rounded to 2 decimal places

# Generate and add 50 random collectors
def add_random_collectors():
    for _ in range(50):
        name = generate_random_name()
        contact_number = generate_random_phone()
        region = generate_random_region()
        total_collected = generate_random_total_collected()

        # Add the collector using the function from `collectors.py`
        add_collector(name, contact_number, region, total_collected)

    print("50 random collectors have been added to the database.")

if __name__ == "__main__":
    add_random_collectors()
