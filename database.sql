-- Product Inventory Database Schema
-- Database: inventory_app

-- Create the database
CREATE DATABASE IF NOT EXISTS inventory_app;
USE inventory_app;

-- Products Table
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample Data for Products
INSERT INTO products (name, description, price, quantity) VALUES
('Laptop', 'High performance laptop', 999.99, 10),
('Mouse', 'Wireless mouse', 29.99, 50),
('Keyboard', 'Mechanical keyboard', 79.99, 25);
