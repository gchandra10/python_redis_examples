from db_config import get_redis_connection

r = get_redis_connection()

r.flushall()

# SET command
r.set("character:rachel", "Fashion")
# GET command
print(f"Reading the Key 'character:rachel' {r.get('character:rachel')}")
# STRLEN command
print(r.strlen("character:rachel"))
# APPEND command
r.append("character:rachel", " Designer")
# GETRANGE command
print(r.getrange("character:rachel", 0, 4))

# SET another character
r.set("character:ross", "Palentologist")

print("-" * 100)

# Use scan to iterate through keys that match 'character:*'
cursor = "0"
while cursor != 0:
    cursor, keys = r.scan(cursor=cursor, match="character:*")
    for key in keys:
        value = r.get(key)
        print(f"{key}: {value}")

print("-" * 100)

print("Following Keys method not recommended in Prod")

# Use keys to find all keys that match 'character:*'
keys = r.keys("character:*")

# Get the values for each key
for key in keys:
    value = r.get(key)
    print(f"{key}: {value}")
