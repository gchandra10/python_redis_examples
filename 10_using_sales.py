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

# Convert bytes to strings in DataFrame (Redis returns bytes)
# df = df.applymap(lambda x: x.decode('utf-8') if isinstance(x, bytes) else x)

# Calculate total profit
df["profit"] = pd.to_numeric(df["TotalProfit"])
total_profit = df["profit"].sum()
etime = time.time()

print(f"Total Profit: {total_profit}, {etime - stime}")


# file_path = (
#     "https://raw.githubusercontent.com/gchandra10/filestorage/main/sales_100.csv"
# )

# # Read the CSV file
# df1 = pd.read_csv(file_path)
# df1['profit'] = pd.to_numeric(df1['TotalProfit'])
# total_profit2 = df1['profit'].sum()
# print(f"Total Profit: {total_profit}")
