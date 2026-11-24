import pandas as pd

df = pd.read_csv('data/raw/olist_order_reviews_dataset.csv')

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Initial inspection
print(df.head())
print(df.info())

# Data quality
print("Duplicate rows:", df.duplicated().sum())

print("Missing values:")
print(df.isnull().sum())

# Review score statistics
print(df['review_score'].describe())

# Review score distribution
print("Review score distribution:")
print(df['review_score'].value_counts().sort_index())

# Unique values
print(df.nunique())