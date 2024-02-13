import pandas as pd

from db_config import get_redis_connection

r = get_redis_connection()

file_path = (
    "https://raw.githubusercontent.com/gchandra10/filestorage/main/sales_100.csv"
)

# Read the CSV file
df = pd.read_csv(file_path)

# Ingest data into Redis
for index, row in df.iterrows():
    # Using the index as part of the key for simplicity; consider a more meaningful key for production
    key = f"sales:{index}"
    # Convert row to a dict and store in Redis
    r.hset(key, mapping=row.to_dict())
