import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# File paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROCESSED_DATA = BASE_DIR / "data" / "processed"

# Load datasets
orders = pd.read_csv(PROCESSED_DATA / "orders.csv")
order_items = pd.read_csv(PROCESSED_DATA / "order_items.csv")

# Merge datasets
df = pd.merge(orders, order_items, on="order_id")

# Keep delivered orders
df = df[df["order_status"] == "delivered"].copy()

# Convert purchase timestamp
df["order_purchase_timestamp"] = pd.to_datetime(
    df["order_purchase_timestamp"]
)

# Calculate monthly revenue
df["month"] = df["order_purchase_timestamp"].dt.to_period("M")

monthly_revenue = (
    df.groupby("month")["price"]
    .sum()
    .reset_index()
)

monthly_revenue["month"] = monthly_revenue["month"].astype(str)

# Create visualisation
plt.figure(figsize=(12, 6))

plt.plot(
    monthly_revenue["month"],
    monthly_revenue["price"],
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (BRL)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save chart
OUTPUT_DIR = BASE_DIR / "visualisations" / "sales"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


plt.savefig(OUTPUT_DIR / "monthly_revenue.png", dpi=300)
plt.show()
