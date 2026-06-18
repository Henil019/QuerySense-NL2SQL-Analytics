import random
import pyodbc

conn=pyodbc.connect(
"DRIVER={SQL Server};"
"SERVER=.\\SQLEXPRESS;"
"DATABASE=QuerySenseDB;"
"Trusted_Connection=yes;"
)

cursor=conn.cursor()

products = {
    1: ["iPhone 16", "Samsung Galaxy S25", "Wireless Earbuds", "Smart Watch", "Bluetooth Speaker"],
    2: ["Denim Jacket", "Cotton T-Shirt", "Formal Shirt", "Hooded Sweatshirt", "Jeans"],
    3: ["Atomic Habits", "Rich Dad Poor Dad", "Clean Code", "The Psychology of Money", "Deep Work"],
    4: ["Coffee Maker", "Mixer Grinder", "Electric Kettle", "Air Fryer", "Rice Cooker"],
    5: ["Yoga Mat", "Cricket Bat", "Football", "Dumbbells", "Tennis Racket"],
    6: ["Face Wash", "Hair Dryer", "Lipstick Set", "Perfume", "Moisturizer"],
    7: ["LEGO Set", "Remote Control Car", "Puzzle Board", "Teddy Bear", "Building Blocks"],
    8: ["Olive Oil", "Green Tea", "Almonds", "Peanut Butter", "Basmati Rice"],
    9: ["Backpack", "Laptop Sleeve", "Wallet", "Sunglasses", "Travel Bag"],
    10: ["Running Shoes", "Sneakers", "Sandals", "Formal Shoes", "Sports Shoes"]
}

for category_id, items in products.items():
    for product in items:
        price=round(random.uniform(100, 50000),2)
        stock=random.randint(10, 200)

        cursor.execute(
        """
        INSERT INTO Products
        (ProductName, CategoryId, Price, StockQuantity)
        VALUES(?, ?, ?, ?)
        """,
        product,
        category_id,
        price,
        stock
        )

conn.commit()
print("Product Added sucesfully!!")
conn.close()