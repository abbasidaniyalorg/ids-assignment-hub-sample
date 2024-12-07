import pandas as pd
import random
import string
from faker import Faker

# Initialize faker instance
faker = Faker()

# Function to generate random alphanumeric IDs
def generate_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

# Generate random data for 1000 records
data = []
for _ in range(1000):
    record = {}
    
    # ID
    record["ID"] = generate_id()
    
    # Name
    name = faker.name()
    if random.random() > 0.5:
        name_parts = name.split()
        if len(name_parts) == 3:
            name = f"{name_parts[0]} {name_parts[2]}"
    record["Name"] = name.upper() if random.random() > 0.5 else name.lower()
    
    # Date of Birth & Age
    if random.random() > 0.05:
        dob = faker.date_of_birth()
        record["Date of Birth"] = dob.strftime("%m/%d/%Y") if random.random() > 0.5 else dob.strftime("%B %d, %Y")
        record["Age"] = (pd.Timestamp.now() - pd.Timestamp(dob)).days // 365
    else:
        record["Date of Birth"] = None
        record["Age"] = None
    
    # Gender
    record["Gender"] = random.choice(["M", "F", "O", None]) if random.random() > 0.05 else None

    # Body Mass Index
    record["Body Mass Index"] = random.uniform(15, 35) if random.random() > 0.1 else None
    
    # Address
    if random.random() > 0.1:
        record["Address"] = f"{faker.street_address()}, {faker.city()}, {faker.state()}, {faker.zipcode()}"
    else:
        record["Address"] = None

    # Weekly Wage
    if random.random() > 0.05:
        record["Weekly wage"] = random.randint(100, 10000)
    else:
        record["Weekly wage"] = random.choice(["5K", "3,423", None])
    
    # Job Status
    record["Job status"] = random.choice(["Student", "Employed", "Unemployed", None]) if random.random() > 0.02 else None

    # Profession
    if record["Job status"] == "Employed":
        record["Profession"] = random.choice(["Engineer", "Teacher", "Doctor", "Designer", "Developer", "Manager"])
    elif random.random() < 0.01:
        record["Profession"] = random.choice(["none", "missing"])
    else:
        record["Profession"] = None

    # Annual Income
    if random.random() > 0.05:
        record["Annual Income"] = random.randint(5000, 500000)
    else:
        record["Annual Income"] = random.choice(["5K", "3,423", None])

    # Email Address
    if random.random() > 0.03:
        record["Email address"] = faker.email()
    else:
        record["Email address"] = random.choice([f"{faker.user_name()}domain.com", f"@{faker.domain_name()}", None])

    # Contact Number
    if random.random() > 0.04:
        record["Contact Number"] = faker.msisdn()
    else:
        record["Contact Number"] = random.choice(["+1(323)-321-1003", "+1685784256", faker.msisdn()[:10]])

    # Marital Status
    record["Marital Status"] = random.choice(["Married", "Unmarried", None]) if random.random() > 0.01 else None

    # Number of Dependents
    if random.random() > 0.02:
        record["# of dependants"] = random.randint(0, 6)
    else:
        record["# of dependants"] = random.choice(["One", "Two", None])

    # Average Monthly Expenditure
    if random.random() > 0.05:
        record["Avg Monthly Expenditure"] = random.randint(50, 500000)
    else:
        record["Avg Monthly Expenditure"] = random.choice(["5K", "3,423", None])
    
    data.append(record)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
file_path = "source/Assignment 1/data/data.csv"
df.to_csv(file_path, index=False)
