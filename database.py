import sqlite3
from datetime import datetime


DB_NAME = "price_tracker.db"


def create_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            url TEXT,
            target_price REAL,
            current_price REAL,
            last_checked TEXT
        )
    """)

    connection.commit()
    connection.close()


def add_product(name, url, target_price, current_price):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO products
        (name, url, target_price, current_price, last_checked)
        VALUES (?, ?, ?, ?, ?)
    """, (
        name,
        url,
        target_price,
        current_price,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    connection.commit()
    connection.close()


def get_products():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    connection.close()

    return products
