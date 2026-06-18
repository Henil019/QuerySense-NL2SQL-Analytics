import pyodbc

conn=pyodbc.connect(
"DRIVER={SQL Server};"
"SERVER=.\\SQLEXPRESS;"
"DATABASE=QuerySenseDB;"
"Trusted_Connection=yes;"
)

cursor=conn.cursor()

categories = [
    "Electronics",
    "Fashion",
    "Books",
    "Home & Kitchen",
    "Sports",
    "Beauty",
    "Toys",
    "Groceries",
    "Accessories",
    "Footwear"
]

for category in categories:
    cursor.execute(
        "INSERT INTO Categories (CategoryName) VALUES(?)",
        category
    )

conn.commit()
print("Categiry Inserted sucessfully")
conn.close();