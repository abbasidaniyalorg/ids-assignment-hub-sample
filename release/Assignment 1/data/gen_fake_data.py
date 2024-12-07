import pandas as pd
import numpy as np
import random
import string
from faker import Faker

# Initialize faker instance
Faker.seed(42)
faker = Faker()
random.seed(42)

# Function to generate random alphanumeric IDs
def generate_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))


def get_dirty_integer(value):
    if random.choice([True, False]):
        # Format with commas (e.g., 3,423)
        return f"{value:,}"
    else:
        # Format with 'K' only if value is 1000 or greater
        if value >= 1000:
            return f"{value // 1000}K"
        else:
            return str(value)  # Keep the original value for numbers less than 1000

# Function to generate a random date of birth based on a normal distribution
def generate_dob(min_age=16, max_age=115, mean_age=45, std_dev_age=20):
    # Generate age using normal distribution
    age = int(np.random.normal(loc=mean_age, scale=std_dev_age))
    
    # Ensure the age is within the specified range
    age = max(min_age, min(age, max_age))
    
    # Calculate the year of birth
    current_year = pd.Timestamp.now().year
    year_of_birth = current_year - age
    
    # Generate a random month and day for the birthdate
    month = np.random.randint(1, 13)
    day = np.random.randint(1, 29)  # Keep it simple by using 28 to avoid month/day issues
    
    # Create the birthdate
    dob = pd.Timestamp(year_of_birth, month, day)
    
    return dob, age


def get_weekly_wage(age):
    # Define age groups and corresponding mean wage and standard deviation
    if age < 20:
        mean_wage = 300  # Lower wage for young age
        std_dev = 50
    elif 20 <= age < 30:
        mean_wage = 700  # Slightly higher for young adults
        std_dev = 100
    elif 30 <= age < 40:
        mean_wage = 1200  # Mid-career wage
        std_dev = 150
    elif 40 <= age < 50:
        mean_wage = 1700  # More experienced professionals
        std_dev = 200
    elif 50 <= age < 60:
        mean_wage = 2200  # Higher wage for more experienced workers
        std_dev = 250
    else:
        mean_wage = 2500  # Senior professionals or retirement age
        std_dev = 300

    # Generate a wage based on a normal distribution
    weekly_wage = int(random.gauss(mean_wage, std_dev))
    
    return weekly_wage

def get_job_status(age):
    if age < 18:
        return "Student"  # Under 18 are typically students, no randomness needed
    elif 18 <= age < 22:
        # 70% chance of being a student, 30% chance of being employed
        return "Student" if random.random() < 0.7 else "Employed"
    elif 22 <= age < 30:
        # 60% chance of being employed, 40% chance of being a student (e.g., graduate students)
        return "Employed" if random.random() < 0.6 else "Student"
    elif 30 <= age < 50:
        # 90% chance of being employed, 10% chance of being unemployed
        return "Employed" if random.random() < 0.9 else "Unemployed"
    elif 50 <= age < 60:
        # 70% chance of being employed, 30% chance of being unemployed
        return "Employed" if random.random() < 0.7 else "Unemployed"
    else:
        # 60% chance of being unemployed, 40% chance of still being employed
        return "Unemployed" if random.random() < 0.6 else "Employed"

def generate_avg_monthly_expenditure(age, weekly_wage):
    # Adjust the mean of the normal distribution based on age and weekly wage
    # Younger people spend more, so we have a higher mean for younger ages and higher wages
    if age < 30:
        mean_expenditure = 10000 + (weekly_wage * 0.5)  # Younger people tend to spend more
    elif age < 60:
        mean_expenditure = 5000 + (weekly_wage * 0.3)  # Middle-aged people tend to have a balanced expenditure
    else:
        mean_expenditure = 2000 + (weekly_wage * 0.2)  # Older people tend to spend less

    # Use a normal distribution with some skew
    std_dev_expenditure = 2000  # Standard deviation of expenditure
    raw_expenditure = int(np.random.normal(loc=mean_expenditure, scale=std_dev_expenditure))

    # Ensure the expenditure is within the valid range (50 to 500,000)
    return max(50, min(raw_expenditure, 500000))

def calculate_bmi(gender, income, age, job_status, marital_status, dependents):
    # Base BMI
    bmi = random.uniform(18.5, 24.9)  # Normal BMI range

    # Adjust BMI based on Gender
    if gender == "M":
        bmi += random.uniform(1, 2)  # Slightly higher BMI for males
    elif gender == "F":
        bmi -= random.uniform(0.5, 1.5)  # Slightly lower BMI for females
    elif gender == "O":
        bmi += random.uniform(-1, 1)  # Neutral adjustment for others

    # Adjust BMI based on Age
    if age and age > 40:
        bmi += random.uniform(1, 3)  # Higher BMI for older individuals

    # Adjust BMI based on Annual Income
    if income and income < 50000:
        bmi += random.uniform(1, 2)  # Higher BMI for lower income
    elif income and income > 100000:
        bmi -= random.uniform(0.5, 1)  # Lower BMI for higher income

    # Adjust BMI based on Job Status
    if job_status == "Unemployed":
        bmi += random.uniform(1, 2)  # Higher BMI for unemployed individuals
    elif job_status == "Student":
        bmi -= random.uniform(0.5, 1)  # Lower BMI for students

    # Adjust BMI based on Marital Status
    if marital_status == "Married":
        bmi += random.uniform(0.5, 1.5)  # Slightly higher BMI for married individuals

    # Adjust BMI based on Number of Dependents
    if dependents and dependents > 2:
        bmi += random.uniform(0.5, 1.5)  # Higher BMI for more dependents

    # Ensure BMI stays within realistic bounds
    return max(15, min(45, bmi))

# Generate random data for 1000 records
data = []
for _ in range(1000):
    record = {}
    
    # ID
    id_ = generate_id()

    if random.random() > 0.95:
        # Duplicate ID
        id_ = random.choice([record["ID"] for record in data])
    
    record["ID"] = id_
    
    # Name
    name = faker.name()
    if random.random() > 0.5:
        name_parts = name.split()
        if len(name_parts) == 3:
            name = f"{name_parts[0]} {name_parts[2]}"
    record["Name"] = name.upper() if random.random() > 0.5 else name.lower()
    
    # Date of Birth & Age
    dob, age = generate_dob()
    if random.random() > 0.05:
        record["Date of Birth"] = dob.strftime("%m/%d/%Y") if random.random() > 0.8 else dob.strftime("%B %d, %Y")
        record["Age"] = age
    elif random.random() > 0.02:
        record["Date of Birth"] = dob.strftime("%m/%d/%Y") if random.random() > 0.8 else dob.strftime("%B %d, %Y")
        record["Age"] = None
    else:
        record["Date of Birth"] = None
        record["Age"] = None

    # Gender
    record["Gender"] = random.choice(["M", "F", "O"])
    
    # Address
    record["Address"] = f"{faker.street_address()}, {faker.city()}, {faker.state()}, {faker.zipcode()}"
    

    # Weekly Wage
    raw_weekly_wage = get_weekly_wage(age)
    record["Weekly wage"] = raw_weekly_wage
    if random.random() <= 0.05:
        record["Weekly wage"] = get_dirty_integer(record["Weekly wage"])
    
    # Job Status
    record["Job status"] = get_job_status(age)

    # Profession
    if record["Job status"] == "Employed":
        record["Profession"] = random.choice(["Engineer", "Teacher", "Doctor", "Designer", "Developer", "Manager"])
    else:
        record["Profession"] = None

    # Annual Income
    raw_annual_wage = raw_weekly_wage * (52 + random.randint(0, 5) + random.random())
    record["Annual Income"] = raw_annual_wage
    if random.random() <= 0.05:
        record["Annual Income"] = get_dirty_integer(record["Annual Income"])

    # Email Address
    if random.random() > 0.03:
        record["Email address"] = faker.email()
    else:
        record["Email address"] = random.choice([f"{faker.user_name()}{faker.domain_name()}", f"@{faker.domain_name()}", f"{faker.user_name()}@"])

    # Contact Number
    if random.random() > 0.04:
        record["Contact Number"] = faker.msisdn()
    else:
        record["Contact Number"] = random.choice(
            [
                f"+1({random.randint(200, 999)})-{random.randint(100, 999)}-{random.randint(1000, 9999)}",  # US number with brackets
                f"+{random.randint(1, 99)}{random.randint(1000000000, 9999999999)}",  # International number
                faker.msisdn()[:10],  # Shortened version of an MSISDN
                f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"  # Local number format
            ]
        )

    # Marital Status
    record["Marital Status"] = random.choice(["Married", "Unmarried"])

    # Number of Dependents
    no_of_dependants = random.randint(0, 6)
    record["# of dependants"] = no_of_dependants
    if random.random() <= 0.05:
        record["# of dependants"] = get_dirty_integer(record["# of dependants"])

    
    # Body Mass Index
    record["Body Mass Index"] = calculate_bmi(record["Gender"], raw_annual_wage, age, record["Job status"], record["Marital Status"], no_of_dependants) if random.random() > 0.05 else None

    # Average Monthly Expenditure
    record["Avg Monthly Expenditure"] = generate_avg_monthly_expenditure(age, raw_weekly_wage)
    if random.random() <= 0.05:
        record["Avg Monthly Expenditure"] = get_dirty_integer(record["Avg Monthly Expenditure"])
    
    data.append(record)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
file_path = "source/Assignment 1/data/data.csv"
df.to_csv(file_path, index=False)
