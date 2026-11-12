import os
import psycopg2
import random

conect = psycopg2.connect(
    host=os.getenv("DB_HOST", "localhost"),
    port=os.getenv("DB_PORT", "5434"),
    dbname="test_db",
    user="test_user",
    password="test_pasword"
)

cursor = conect.cursor()

gadgets = [
    "iPhone 15",
    "Samsung Galaxy S24",
    "MacBook Air",
    "iPad Air",
    "AirPods Pro"
]
categories = [
    "Smartphones",
    "Laptops",
    "Tablets",
    "Headphones"]


def creation_table_1():
    Create_table = f"""CREATE TABLE IF NOT EXISTS products (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
    Name TEXT, 
    Price INTEGER,
    Description TEXT, 
    Type_category INTEGER,
    FOREIGN KEY (Type_category) REFERENCES categories(id)

    )"""

    cursor.execute(Create_table)
    conect.commit()


def creation_table_2():
    Create_table = f"""CREATE TABLE IF NOT EXISTS categories (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Name TEXT)
"""
    cursor.execute(Create_table)
    conect.commit()


def generate_data_table_1():
    for name in gadgets:
        if name == "iPhone 15":
            cat = 1
        elif name == "Samsung Galaxy S24":
            cat = 1
        elif name == "MacBook Air":
            cat = 2
        elif name == "iPad Air":
            cat = 3
        else:
            cat = 4
        gen = f"""INSERT INTO products 
        (Name, Price, Description, Type_Category) VALUES 
        ('{name}', {random.randint(100, 2000)}, 'Ololo', {cat})"""
        cursor.execute(gen)
    conect.commit()


def generate_data_table_2():
    for name in categories:
        gen = f"""INSERT INTO categories
        (Name) VALUES 
        ('{name}')"""
        cursor.execute(gen)
    conect.commit()


def joining():
    j = """SELECT categories.Name, 
    products.Description FROM 
    categories JOIN 
    products ON products.Type_category = categories.id """
    cursor.execute(j)
    conect.commit()
    result = cursor.fetchall()

    for row in result:
        print(row)


def start():
    (creation_table_2(),
     creation_table_1(),
     generate_data_table_2(),
     generate_data_table_1(),
     joining())


start()


