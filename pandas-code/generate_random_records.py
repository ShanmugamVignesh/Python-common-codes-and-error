"""
Used to generate excel data contains random values (Zone- India)
"""

# pip install pandas
# pip install faker
# pip install openpyxl
import pandas as pd
import faker

fake = faker.Faker('en_IN')  # Zone
range_data = 400  # Record count
data = {
    'First Name': [fake.first_name() for _ in range(range_data)],
    'Last Name': [fake.last_name() for _ in range(range_data)],
    'Middle Name': [fake.first_name() for _ in range(range_data)],
    'PAN': [fake.random_int(min=1000000000, max=9999999999) for _ in range(range_data)],
    'Mobile Number': [fake.phone_number() for _ in range(range_data)],
    'Address': [fake.street_address() for _ in range(range_data)],
    'City': [fake.city() for _ in range(range_data)],
    'State': [fake.state() for _ in range(range_data)],
    'District': [fake.city_suffix() for _ in range(range_data)],
    'Pincode': [fake.postcode() for _ in range(range_data)],
    'Email': [fake.email() for _ in range(range_data)],
    'DOB': [fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d') for _ in range(range_data)]
}  # columns
df = pd.DataFrame(data)
df.to_excel('random_data.xlsx', index=False)  # save as excel
