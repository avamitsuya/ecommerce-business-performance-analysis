import pandas as pd 
from pathlib import Path 

#Define the porject path 

BASE_DIR = Path(__file__).resolve().parent.parent.parent
RAW_DATA = BASE_DIR /"data"/"raw"
PROCESSED_DATA = BASE_DIR /"data"/"processed"

# 1. Clean the orders dataset 
orders = pd.read_csv(RAW_DATA/"olist_orders_dataset.csv")

# Convert date columns 
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]
for column in date_columns:
    orders[column] = pd.to_datetime(orders[column], errors="coerce")

# Sava the processed dataset 
orders.to_csv(PROCESSED_DATA/"orders.csv", index=False)

# 2. Prepare the products dataset 
products = pd.read_csv(RAW_DATA/"olist_products_dataset.csv")
products.to_csv(PROCESSED_DATA/"products.csv", index=False)

# 3. Prepare the order item dataset 
order_items = pd.read_csv(RAW_DATA/"olist_order_items_dataset.csv")
order_items["shipping_limit_date"] = pd.to_datetime(
    order_items["shipping_limit_date"], errors="coerce"
    )
order_items.to_csv(PROCESSED_DATA/"order_items.csv", index=False)

# 4. Prepare the payment dataset 
payments = pd.read_csv(RAW_DATA/"olist_order_payments_dataset.csv")
payments.to_csv(PROCESSED_DATA/"order_payments.csv", index=False)

# 5. Prepare the reviews dataset
reviews = pd.read_csv(RAW_DATA / "olist_order_reviews_dataset.csv")

review_date_columns = [
    "review_creation_date",
    "review_answer_timestamp"
]

for column in review_date_columns:
    reviews[column] = pd.to_datetime(
        reviews[column], errors="coerce"
    )

reviews.to_csv(PROCESSED_DATA / "order_reviews.csv", index=False)

# 6. Prepare the sellers dataset 
sellers = pd.read_csv(RAW_DATA / "olist_sellers_dataset.csv")

sellers.to_csv(PROCESSED_DATA / "sellers.csv", index=False)

# 7. Clean the geolocation datset 

geolocation = pd.read_csv(RAW_DATA / "olist_geolocation_dataset.csv")

geolocation = geolocation.drop_duplicates()

# Save processed dataset
geolocation.to_csv(
    PROCESSED_DATA / "geolocation.csv",
    index=False
)
# 8. Prepare the customers dataset

customers = pd.read_csv(RAW_DATA / "olist_customers_dataset.csv")
customers.to_csv(PROCESSED_DATA / "customers.csv", index=False)


# 9. Prepare the category translation dataset

translation = pd.read_csv(RAW_DATA / "product_category_name_translation.csv")
translation.to_csv(PROCESSED_DATA / "category_translation.csv", index=False)