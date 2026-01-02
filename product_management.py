from db_connection import get_connection

# CREATE - Add a new product
def create_product(name, description, price, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO products (name, description, price, quantity) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, description, price, quantity))
    conn.commit()
    cursor.close()
    conn.close()

# READ - Get all products
def get_all_products():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM products"
    cursor.execute(query)
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return products

# READ - Get a single product by ID
def get_product_by_id(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM products WHERE id = %s"
    cursor.execute(query, (product_id,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()
    return product

# UPDATE - Update a product
def update_product(product_id, name, description, price, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE products SET name = %s, description = %s, price = %s, quantity = %s WHERE id = %s"
    cursor.execute(query, (name, description, price, quantity, product_id))
    conn.commit()
    cursor.close()
    conn.close()

# DELETE - Delete a product
def delete_product(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM products WHERE id = %s"
    cursor.execute(query, (product_id,))
    conn.commit()
    cursor.close()
    conn.close()
