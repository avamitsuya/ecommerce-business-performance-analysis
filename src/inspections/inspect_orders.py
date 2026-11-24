
import pandas as pd

# Load the dataset
df = pd.read_csv('data/raw/olist_orders_dataset.csv')

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print(df.head())
print(df.info())

# ----------------------------------
# DATA QUALITY INSPECTION
# ----------------------------------

# 1. Check duplicate records
print("Duplicated rows:", df.duplicated().sum())

# Check duplicate order IDs
print("Duplicated order IDs:", df['order_id'].duplicated().sum())

# 2. Check missing values
print("Missing values per column:")
print(df.isnull().sum())

print("Total missing values:", df.isnull().sum().sum())

# 3. Check data types
print("Data types:")
print(df.dtypes)

# 4. Check order statuses
print("Order status distribution:")
print(df['order_status'].value_counts(dropna=False))

# ----------------------------------
# DATA PREPARATION
# ----------------------------------

date_columns = [
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
]

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# ----------------------------------
# ORDER ANALYSIS
# ----------------------------------

# 1. How long does payment approval take?
df['approval_time'] = (
    df['order_approved_at'] -
    df['order_purchase_timestamp']
)

print(
    "Average payment approval time:",
    df['approval_time'].mean()
)

# 2. What is the average delivery time?
df['delivery_time'] = (
    df['order_delivered_customer_date'] -
    df['order_purchase_timestamp']
)

print(
    "Average delivery time:",
    df['delivery_time'].mean()
)

# 3. How often are orders early or late?

df['delivery_difference'] = (
    df['order_delivered_customer_date'].dt.normalize() -
    df['order_estimated_delivery_date'].dt.normalize()
)

# Classify delivery performance
delivered = df['order_delivered_customer_date'].notna()

df.loc[delivered, 'delivery_status'] = 'On time'

df.loc[
    delivered & (df['delivery_difference'] < pd.Timedelta(0)),
    'delivery_status'
] = 'Early'

df.loc[
    delivered & (df['delivery_difference'] > pd.Timedelta(0)),
    'delivery_status'
] = 'Late'

print("Delivery performance (%):")

print(
    df.loc[delivered, 'delivery_status']
    .value_counts(normalize=True) * 100
)

print("Total orders:", len(df))
print("Delivered orders:", delivered.sum())
print("Orders excluded:", (~delivered).sum())
