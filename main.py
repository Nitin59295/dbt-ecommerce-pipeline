import psycopg2
import requests
import json

conn = psycopg2.connect(
    host = "localhost",
    port = 5432,
    dbname = "ecommerce_v2",
    user = "postgres",
    password = "1011"
)
cur = conn.cursor()

#____FETCHING DATA FROM FAKE STORE API's

print("Fetching data from the FAKE STORE API ")
products = requests.get("https://fakestoreapi.com/products").json()
users = requests.get(" https://fakestoreapi.com/users").json()
carts = requests.get(" https://fakestoreapi.com/carts").json()
print(f"Products: {len(products)}")
print(f"Users: {len(users)}")
print(f"Carts: {len(carts)}")

#______CREATING RAW TABLES FOR PRODUCTS,USERS,CARTS

#---PRODUCTS

cur.execute("DROP TABLE IF EXISTS raw_products CASCADE")
cur.execute("""
        CREATE TABLE raw_products(
            id INTEGER,
            title TEXT,
            price NUMERIC,
            category TEXT,
            description TEXT,
            rating_rate NUMERIC,
            rating_count NUMERIC 
        );
""")

#----USERS
cur.execute("DROP TABLE IF EXISTS raw_users CASCADE")
cur.execute("""
    CREATE TABLE raw_users (
        id INTEGER,
        email TEXT,
        username TEXT,
        firstname TEXT,
        lastname TEXT,
        city TEXT,
        zipcode TEXT,
        phone TEXT
    );
""")

#----CARTS
cur.execute("DROP TABLE IF EXISTS raw_carts CASCADE")
cur.execute("""
    CREATE TABLE raw_carts (
        id INTEGER,
        user_id INTEGER,
        date TEXT,
        product_id INTEGER,
        quantity INTEGER
    );
""")

#____LOADING DATA

#--- FOR PRODUCTS
for p in products:
    cur.execute("""
        INSERT INTO raw_products VALUES(%s,%s,%s,%s,%s,%s,%s)
""",(
        p["id"],p["title"],p["price"],p["category"],
        p["description"],p["rating"]["rate"],p["rating"]["count"]
    ))

#--- FOR USERS
for u in users:
    cur.execute("""INSERT INTO raw_users VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
            u["id"],u["email"],u["username"],u["name"]["firstname"],
            u["name"]["lastname"],u["address"]["city"],u["address"]["zipcode"],u["phone"],
    ))

#--- FOR CARTS

for c in carts:
    for item in c["products"]:
        cur.execute("""INSERT INTO raw_carts VALUES(%s,%s,%s,%s,%s) 
    """,  (
            c["id"],c["userId"],c["date"],
            item["productId"],item["quantity"]
    ))

conn.commit()
cur.close()
conn.close()
print("\n All the raw tables loaded into Postgres ")





