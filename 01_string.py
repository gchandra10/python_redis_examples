from db_config import get_redis_connection

r = get_redis_connection()

# Clear the DB
r.flushall()

## Store a String Key
r.set("name", "Rachel")

## Display the Data Type
print(r.type("name"))

## Retrive the String Key
print(r.get("name"))
