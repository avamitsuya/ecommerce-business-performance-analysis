import pandas as pd

# Data loading 
df = pd.read_csv('data/raw/olist_customers_dataset.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print(df.head())
print(df.shape)

# Data inspection 
#1- Which state has the most customers? 
print(df['customer_state'].value_counts().head())
#2- How many different cities are represented? 
print(df['customer_city'].nunique())
#3- How many unique customers are reprsented?
print(df['customer_unique_id'].nunique())

print(df.info())
print("Duplicated values: ", df.duplicated().sum())
print(df['customer_id'].str.len().value_counts())
print(df['customer_state'].unique())
print(df['customer_zip_code_prefix'].describe())
print("Customer IDs:", df['customer_id'].nunique())
print("Unique customers:", df['customer_unique_id'].nunique())