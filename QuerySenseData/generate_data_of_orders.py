import pyodbc
import random
from faker import Faker

fake=Faker()

conn=pyodbc.connect(
"DRIVER={SQL Server};"
"SERVER=.\\SQLEXPRESS;"
"DATABASE=QuerySenseDB;"
"Trusted_Connection=yes;"

)

cursor=conn.cursor()


for i in range(500):
    customer_id=random.randint(1, 100)
    order_date=fake.date_time_between(
    start_date='-12M',
    end_date='now'
    )
    total_amount=round(random.uniform(500, 50000),2)
    cursor.execute(
    """
    INSERT INTO Orders
    (CustomerId, OrderDate, TotalAmount)
    VALUES(?, ?, ?)
    """,
    customer_id,
    order_date,
    total_amount

    )
conn.commit()

print("Order inserted")
conn.close()