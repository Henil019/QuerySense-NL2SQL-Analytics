from faker import Faker
import random
import pyodbc

fake=Faker()

conn=pyodbc.connect(
"DRIVER={SQL SERVER};"
"SERVER=.\\SQLEXPRESS;"
"DATABASE=QuerySenseDB;"
"Trusted_Connection=yes;"
)

cursor=conn.cursor()

cities = [
    "Mumbai",
    "Delhi",
    "Ahmedabad",
    "Pune",
    "Bangalore",
    "Hyderabad",
    "Chennai",
    "Kolkata",
    "Jaipur",
    "Surat"
]

for i in range(100):
    name=fake.name()
    email=fake.unique.email()
    city=random.choice(cities)
    country="India"

    cursor.execute(
    """
    INSERT INTO Customers
    (CustomerName, Email, City, Country) 
    VALUES(?, ?, ?, ?)
    """,
    name, 
    email,
    city, 
    country
    )

conn.commit()
print("100 customers added sucessfully!!")

conn.close()