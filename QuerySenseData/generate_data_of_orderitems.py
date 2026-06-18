import pyodbc
import random

conn = pyodbc.connect(
"DRIVER={SQL Server};"
"SERVER=.\\SQLEXPRESS;"
"DATABASE=QuerySenseDB;"
"Trusted_Connection=yes;"
)

cursor = conn.cursor()

cursor.execute("SELECT OrderId FROM Orders")
orders = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT ProductId FROM Products")
product_ids = [row[0] for row in cursor.fetchall()]

for order_id in orders:

    total_amount = 0

    number_of_items = random.randint(1, 4)

    used_products = set()

    for i in range(number_of_items):

        while True:
            product_id = random.choice(product_ids)

            if product_id not in used_products:
                used_products.add(product_id)
                break

        # Get the product price
        cursor.execute(
            """
            SELECT Price
            FROM Products
            WHERE ProductId = ?
            """,
            product_id
        )

        row = cursor.fetchone()

        # Safety check
        if row is None:
            print("Product not found:", product_id)
            continue

        price = float(row[0])

        # Generate quantity
        quantity = random.randint(1, 5)

        # Calculate total amount
        total_amount += price * quantity

        # Insert into OrderItems
        cursor.execute(
            """
            INSERT INTO OrderItems
            (OrderId, ProductId, Quantity, UnitPrice)
            VALUES (?, ?, ?, ?)
            """,
            order_id,
            product_id,
            quantity,
            price
        )

    # Update actual order total
    cursor.execute(
        """
        UPDATE Orders
        SET TotalAmount = ?
        WHERE OrderId = ?
        """,
        round(total_amount, 2),
        order_id
    )

# Save changes
conn.commit()

print("OrderItems inserted successfully!")
print("Order totals updated successfully!")

conn.close()