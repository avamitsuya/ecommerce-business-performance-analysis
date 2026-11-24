import pandas as pd

df = pd.read_csv('data/raw/olist_order_items_dataset.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Initial inspection
print(df.head())
print(df.info())

# Data quality
print("Duplicate rows:", df.duplicated().sum())
print("Missing values:")
print(df.isnull().sum())

# Numerical statistics
print(df.describe())

# Unique values
print(df.nunique())

#Data inspection 
# Which product is ordered the most? 
product_orders = df['product_id'].value_counts()
print("10 most popular products: ")
print(product_orders.head(10))

# Which seller is the most popular?
seller_orders = df['seller_id'].value_counts()
print("10 most popular sellers")
print(seller_orders.head(10))