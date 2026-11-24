
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

# Filter delivered orders and valid categories
df = df[
    (df["order_status"] == "delivered") &
    (df["product_category_name_english"].notna())
].copy()

# Extract month
df["month"] = pd.to_datetime(
    df["order_purchase_timestamp"]
).dt.to_period("M").astype(str)

# Calculate monthly category revenue
monthly_revenue = df.pivot_table(
    index="product_category_name_english",
    columns="month",
    values="price",
    aggfunc="sum",
    fill_value=0
)

# Keep the top 10 categories overall
top_categories = monthly_revenue.sum(axis=1).nlargest(10).index
monthly_revenue = monthly_revenue.loc[top_categories]

# Convert revenue to thousands of BRL
monthly_revenue = monthly_revenue / 1000

# Create heatmap
fig, ax = plt.subplots(figsize=(16, 8))

heatmap = ax.imshow(
    monthly_revenue,
    aspect="auto",
    cmap="YlOrRd"
)

ax.set_title("Monthly Revenue by Top 10 Product Categories")
ax.set_xlabel("Month")
ax.set_ylabel("Product Category")

ax.set_xticks(range(len(monthly_revenue.columns)))
ax.set_xticklabels(monthly_revenue.columns, rotation=45, ha="right")

ax.set_yticks(range(len(monthly_revenue.index)))
ax.set_yticklabels(monthly_revenue.index)

colorbar = fig.colorbar(heatmap, ax=ax)
colorbar.set_label("Revenue (BRL thousands)")

plt.tight_layout()

# Save chart
OUTPUT_DIR = BASE_DIR / "visualisations" / "products"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

plt.savefig(OUTPUT_DIR / "monthly_category_revenue.png", dpi=300)
