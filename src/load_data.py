import pandas as pd 
from pathlib import Path 
from sqlalchemy import create_engine, URL 
import os 

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DATA = BASE_DIR /"data" / "processed"

connection_url = URL.create(
    drivername = "postgresql+pg8000",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host="localhost",
    port=5432,
    database="ecommerce_analysis"
)

engine = create_engine(connection_url)

datasets = {
    "orders.csv":"orders",
    "products.csv":"products",
    "order_items.csv": "order_items",
    "order_payments.csv": "order_payments",
    "order_reviews.csv": "order_reviews",
    "sellers.csv": "sellers",
    "geolocation.csv": "geolocation",
    "customers.csv": "customers",
    "category_translation.csv": "category_translation"
}

for file_name, table_name in datasets.items():
    file_path = PROCESSED_DATA / file_name
    df = pd.read_csv(file_path)

    df.to_sql(
        name = table_name,
        con = engine,
        if_exists = "fail",
        index = False,
        chunksize = 5000,
        method = "multi"
    )

    print (f"Loaded {table_name} : {len(df)} rows")

engine.dispose()

print("All datasets loaded sucessfully")