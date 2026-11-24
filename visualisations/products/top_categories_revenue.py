
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# File paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data" / "processed"

# Load datasets
orders = pd.read_csv(DATA_DIR / "orders.csv")
items = pd.read_csv(DATA_DIR / "order_items.csv")
products = pd.read_csv(DATA_DIR / "products.csv")
translation = pd.read_csv(DATA_DIR / "category_translation.csv")

# Merge datasets
df = orders.merge(items, on="order_id")
df = df.merge(products, on="product_id")
df = df.merge(translation, on="product_category_name", how="left")

# Filter delivered orders
df = df[df["order_status"] == "delivered"]

# Calculate revenue by category
category_revenue = (
    df.groupby("product_category_name_english")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Create chart
plt.figure(figsize=(12, 7))

category_revenue.sort_values().plot(kind="barh")

plt.title("Top 10 Product Categories by Revenue")
plt.xlabel("Revenue (BRL)")
plt.ylabel("Product Category")
plt.tight_layout()

# Save chart
OUTPUT_DIR = BASE_DIR / "visualisations" / "products"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

plt.savefig(OUTPUT_DIR / "top_categories_revenue.png", dpi=300)
