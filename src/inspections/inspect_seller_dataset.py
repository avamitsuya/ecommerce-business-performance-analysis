import pandas as pd

df = pd.read_csv('data/raw/olist_sellers_dataset.csv')

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Initial inspection
print(df.head())
print(df.info())

# Data quality
print("Duplicate rows:", df.duplicated().sum())

print("Missing values:")
print(df.isnull().sum())

# Unique values
print(df.nunique())

# Seller distribution by state
print("Sellers by state:")
print(df['seller_state'].value_counts())