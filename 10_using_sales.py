import pandas as pd
from db_config import get_redis_connection
import time

r = get_redis_connection()

stime = time.time()
# Assuming you have keys structured as sales:index
keys = r.keys("sales:*")

# Retrieve and convert data to a pandas DataFrame
data = []
for key in keys:
    data.append(r.hgetall(key))

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(data)

# Calculate total profit
df["profit"] = pd.to_numeric(df["TotalProfit"])
total_profit = df["profit"].sum()
etime = time.time()

print(f"Total Profit: {total_profit}, {etime - stime}")
