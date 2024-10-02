import pandas as pd

from db_config import get_redis_connection

r = get_redis_connection()

file_path = (
    "https://raw.githubusercontent.com/gchandra10/filestorage/main/sales_100.csv"
)

## Read the CSV file
df = pd.read_csv(file_path)

# Ingest data into Redis
for index, row in df.iterrows():
    # Using the index as part of the key for simplicity; consider a more meaningful key for production
    key = f"sales:{index}"
    # Convert row to a dict and store in Redis
    r.hset(key, mapping=row.to_dict())

# Get all keys matching a specific pattern
keys = r.keys("sales:*")
print(keys)


## Retrieve a specific record by key
key = "sales:0"
sales_record = r.hgetall(key)
sales_record = {k: v for k, v in sales_record.items()}
print(f"\n first row {sales_record}")


## Get a specific field value from a record
# item_type = r.hget("sales:0", "Item Type")
# print(f"\n Item Type {item_type}")


## Get all sales records
# keys = r.keys("sales:*")
# all_sales = []

# for key in keys:
#     record = r.hgetall(key)
#     record = {k: v for k, v in record.items()}
#     all_sales.append(record)

# # Display all records
# for sale in all_sales:
#     print(sale)



## Get a specific field for all sales records
# keys = r.keys("sales:*")
# total_profit_list = []

# for key in keys:
#     total_profit = r.hget(key, "TotalProfit")
#     total_profit_list.append(total_profit)

# print(total_profit_list)


## Update a field in a sales record
# r.hset("sales:0", "total_sales", "5000.00")
# r.hset("sales:0", "UnitCost", "7.10")

# key = "sales:0"
# sales_record = r.hgetall(key)
# sales_record = {k: v for k, v in sales_record.items()}
# print(f"\n first row after update {sales_record}")


## Delete a specific sales record

# r.delete("sales:0")
# key = "sales:0"
# sales_record = r.hgetall(key)
# sales_record = {k: v for k, v in sales_record.items()}
# print(f"\n first row after delete {sales_record}")