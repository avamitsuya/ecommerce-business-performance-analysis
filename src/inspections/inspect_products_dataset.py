import pandas as pd

df = pd.read_csv('data/raw/olist_products_dataset.csv')

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

# Product category counts
print("Unique product categories:", df['product_category_name'].nunique())