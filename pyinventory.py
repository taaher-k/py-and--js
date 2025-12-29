import mysql.connector

# Step 1: Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",      # Change if needed
    user="root",           # Your MySQL username
    password="Taaher@123#", # Your MySQL password
    database="pyinventroy"
)

cursor = conn.cursor()

# Step 2: Functions for CRUD operations

def create_product():
    pid = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    category = input("Enter Product Category: ")
    try:
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Product Quantity: "))
    except ValueError:
        print("❌ Price must be a number and Quantity must be an integer.")
        return
    
    try:
        cursor.execute(
            "INSERT INTO inventory (iid, iname, iCategory, Price, Quantity) VALUES (%s, %s, %s, %s, %s)",
            (pid, name, category, price, quantity)
        )
        conn.commit()
        print("✅ Product added successfully!")
    except mysql.connector.Error as e:
        print("❌ Error:", e)

def read_product():
    choice = input("Enter Product ID to view details or 'all' to list all products: ")
    if choice.lower() == "all":
        cursor.execute("SELECT * FROM inventory")
        rows = cursor.fetchall()
        if not rows:
            print("⚠️ Inventory is empty.")
        else:
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Category: {row[2]}, Price: {row[3]}, Quantity: {row[4]}")
    else:
        cursor.execute("SELECT * FROM inventory WHERE iID = %s", (choice,))
        row = cursor.fetchone()
        if row:
            print(f"ID: {row[0]}, Name: {row[1]}, Category: {row[2]}, Price: {row[3]}, Quantity: {row[4]}")
        else:
            print("❌ Product not found.")

def update_product():
    pid = input("Enter Product ID to update: ")
    try:
        price = float(input("Enter new Price: "))
        quantity = int(input("Enter new Quantity: "))
        cursor.execute(
            "UPDATE inventory SET Price = %s, Quantity = %s WHERE iID = %s",
            (price, quantity, pid)
        )
        conn.commit()
        if cursor.rowcount > 0:
            print("✅ Product updated successfully!")
        else:
            print("❌ Product not found.")
    except ValueError:
        print("❌ Price must be a number and Quantity must be an integer.")

def delete_product():
    choice = input("Enter Product ID or Name to delete: ")
    # Try delete by ID
    cursor.execute("DELETE FROM inventory WHERE iid = %s", (choice,))
    conn.commit()
    if cursor.rowcount > 0:
        print("✅ Product deleted successfully!")
        return
    # Try delete by Name
    cursor.execute("DELETE FROM inventory WHERE iName = %s", (choice,))
    conn.commit()
    if cursor.rowcount > 0:
        print("✅ Product deleted successfully!")
    else:
        print("❌ Product not found.")









# Step 3: Menu-driven loop
while True:
    print("\n--- Inventory Management System (MySQL) ---")
    print("1. Create Product")
    print("2. Read Product(s)")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        create_product()
    elif choice == "2":
        read_product()
    elif choice == "3":
        update_product()
    elif choice == "4":
        delete_product()
    elif choice == "5":
        print("👋 Exiting Inventory Management System. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")

# Close connection when done
cursor.close()
conn.close()
