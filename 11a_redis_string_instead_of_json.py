from db_config import get_redis_connection
import json
import time

# Read JSON data from a file
with open('tv_show_characters.json', 'r') as file:
    data = file.read()

r = get_redis_connection()

r.flushall()

# Store data as string in Redis
r.set("friends:character", data)

start_time = time.time()

# Get data and decode
string_data = r.get("friends:character")
data = json.loads(string_data)

# Extract fields
# Extract only necessary fields
name = data["jerry"]["name"]
occupation = data["jerry"]["occupation"]
education = data["jerry"]["education"]

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Name: {name}")
print(f"Occupation: {occupation}")
print(f"Education: {education}")
# print(f"Time taken to read data: {elapsed_time} seconds")