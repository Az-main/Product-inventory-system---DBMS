# Product Inventory System

A simple Product Inventory application built with **Python**, **Streamlit**, and **MySQL**.

## Features

- **Product Inventory Module**
  - Add new products
  - View all products
  - Update product details
  - Delete products

## Requirements

- Python 3.8 or higher
- MySQL Server (XAMPP, WAMP, or MySQL Workbench)

## Installation Steps

### Step 1: Install Python Packages

Open terminal/command prompt in this folder and run:

```bash
pip install -r requirements.txt
```

### Step 2: Start MySQL Server

- If using **XAMPP**: Open XAMPP and start MySQL
- If using **WAMP**: Open WAMP and ensure MySQL is running
- If using **MySQL Workbench**: Ensure MySQL service is running

### Step 3: Update Database Configuration

Open `db_connection.py` and `setup_database.py` files.

Ensure the password matches YOUR MySQL password. Currently set to `NewPass123`.

```python
password="YOUR_mysql_PASSWORD"
```

### Step 4: Create Database

Run this command once to create the database and tables:

```bash
python setup_database.py
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at: **http://localhost:8501**

## Project Structure

```
Product_Inventory_App/
├── app.py                  # Main Streamlit application
├── db_connection.py        # MySQL database connection
├── setup_database.py       # Database setup script
├── product_management.py   # Product operations
├── database.sql            # SQL schema file
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Troubleshooting

**Error: Access denied for user 'root'@'localhost'**
- Make sure to update the password in `db_connection.py` and `setup_database.py` to match your MySQL password.

## Author

DBMS Lab Assignment - 7th Trimester
