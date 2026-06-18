from flask import Flask, request, jsonify
import requests
import pyodbc
from flask_cors import CORS

conn=pyodbc.connect(
"DRIVER={SQL Server};"
"SERVER=.\\SQLEXPRESS;"
"DATABASE=QuerySenseDB;"
"Trusted_Connection=yes;"
)
cursor=conn.cursor()


app=Flask(__name__)
CORS(app)

Schema="""
Tables:
Customers(CustomerId, CustomerName, Email, City, Country, CreatedDate)

Categories(CategoryId, CategoryName) 

Products(ProductId, ProductName, CategoryId, Price, StockQuantity)

Orders(OrderId, CustomerId, OrderDate, TotalAmount)

OrderItems(OrderItemId, OrderId, ProductId, Quantity, UnitPrice)
"""

@app.route('/ask', methods=['POST'])


def ask():
    question=request.json['question']
    prompt=f"""
    You are a Microsoft SQL Server and Expert in writing any SQL syntax.

    Rules:
    1. Generate ONLY SQL Server queries.
    2. Use TOP instead of LIMIT.
    3. Never use MySQL syntax.
    4. Return only executable SQL.
    5. Do not use markdown.
    6. Strictly Do not use ```sql at starting of response.
    7. Output only the query text.
    8. There is no limit in writing any charatcters.
    9. If you do not know the answer then just display related records of the table.
    10. Use only give Schema and do not take any schema by yourself.


    Databse Schema:
    {Schema}
    Generate Only SQL.
    
    Question:
    {question}
    """
    response=requests.post(
        "http://localhost:11434/api/generate",
        json={
        "model":"phi3",
        "prompt":prompt,
        "stream":False
        }
    )
   

    sql=response.json()['response']
    sql=sql.replace("```sql","")
    sql=sql.replace("```", "").strip()
    print(sql)
    sqle=sql.upper()

    if not sqle.startswith("SELECT"):
        return jsonify({
        "error":"Only select query allowed"
        })
   

    cursor.execute(sql)

    columns = []
    
    for column in cursor.description:
        columns.append(column[0])

    rows = cursor.fetchall()

    result = []

    for row in rows:
        result.append(list(row))

    return jsonify({
        "sql": sql,
        "columns": columns,
        "data": result
    })

    

if __name__=='__main__':
    app.run(port=5000)