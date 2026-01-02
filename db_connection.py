import mysql.connector
import streamlit as st

def get_connection():
    """Create and return a MySQL database connection."""
    
    # Check if running on Streamlit Cloud with secrets
    if "mysql" in st.secrets:
        config = st.secrets["mysql"]
        return mysql.connector.connect(
            host=config["host"],
            port=config.get("port", 3306),
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        
    # Fallback to local connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="NewPass123",
        database="inventory_app"
    )
    return connection
