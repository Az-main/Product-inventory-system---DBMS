"""
Database Setup Script
Run this once to create the database and tables.
"""
import mysql.connector

# Connect to MySQL (without specifying database first)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NewPass123"
)
cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS inventory_app")
cursor.execute("USE inventory_app")

# Create products table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        description TEXT,
        price DECIMAL(10, 2) NOT NULL,
        quantity INT NOT NULL DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# Check if products table is empty, then add sample data
cursor.execute("SELECT COUNT(*) FROM products")
if cursor.fetchone()[0] == 0:
    cursor.execute("""
        INSERT INTO products (name, description, price, quantity) VALUES
        ('Laptop', 'High performance laptop', 999.99, 10),
        ('Mouse', 'Wireless mouse', 29.99, 50),
        ('Keyboard', 'Mechanical keyboard', 79.99, 25)
    """)

conn.commit()
cursor.close()
conn.close()

print("✅ Database 'inventory_app' setup completed successfully!")
print("✅ Table 'products' created!")
print("✅ Sample data inserted!")
print("\nYou can now run the app with: streamlit run app.py")
