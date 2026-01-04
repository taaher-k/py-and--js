from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import mysql.connector
import os

app = FastAPI()

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Taaher@123#",
    database="pyinventroy"   # ✅ updated database name
)
cursor = conn.cursor(dictionary=True)

# Create Product
@app.post("/products/")
def create_product(product: dict):
    try:
        cursor.execute(
            "INSERT INTO inventory (iid, iname, icategory, price, quantity) VALUES (%s,%s,%s,%s,%s)",
            (product["iid"], product["iname"], product["icategory"], product["price"], product["quantity"])
        )
        conn.commit()
        return {"message": "Product added successfully!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Read All Products
@app.get("/products/")
def read_products():
    cursor.execute("SELECT * FROM inventory")
    return cursor.fetchall()

# Read Single Product
@app.get("/products/{iid}")
def read_product(iid: int):
    cursor.execute("SELECT * FROM inventory WHERE iid=%s", (iid,))
    product = cursor.fetchone()
    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")

# Update Product
@app.put("/products/{iid}")
def update_product(iid: int, product: dict):
    cursor.execute(
        "UPDATE inventory SET price=%s, quantity=%s WHERE iid=%s",
        (product["price"], product["quantity"], iid)
    )
    conn.commit()
    if cursor.rowcount > 0:
        return {"message": "Product updated successfully!"}
    raise HTTPException(status_code=404, detail="Product not found")

# Delete Product
@app.delete("/products/{iid}")
def delete_product(iid: int):
    cursor.execute("DELETE FROM inventory WHERE iid=%s", (iid,))
    conn.commit()
    if cursor.rowcount > 0:
        return {"message": "Product deleted successfully!"}
    raise HTTPException(status_code=404, detail="Product not found")







# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/", response_class=HTMLResponse)
def serve_home():
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        return f.read()
