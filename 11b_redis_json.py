from db_config import get_redis_connection
import json
import time

# Read JSON data from a file
with open('tv_show_characters.json', 'r') as file:
    data = json.load(file)

r = get_redis_connection()

r.flushall()

# Store JSON data in Redis
r.json().set("friends:characters", ".", data)

## This part is to retrieve only necessary fields with timer

start_time = time.time()

# Get only necessary fields from Redis
name = r.json().get("friends:characters", ".jerry.name")
occupation = r.json().get("friends:characters", ".jerry.occupation")
education = r.json().get("friends:characters", ".jerry.education")

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Name: {name}")
print(f"Occupation: {occupation}")
print(f"Education: {education}")
# print(f"Time taken to read data: {elapsed_time} seconds")