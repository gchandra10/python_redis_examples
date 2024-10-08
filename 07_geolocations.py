from db_config import get_redis_connection

r = get_redis_connection()

# clear the memory
r.flushall()

file_path = "./njcities-lat-long.txt"

# Key to store geospatial data in Redis
geo_key = "nj_cities"

with open(file_path, "r") as file:
    next(file)  # Skip the header
    for line in file:
        # Parse each line
        location, latitude, longitude = line.strip().split("\t")
        # Convert latitude and longitude to float
        latitude, longitude = float(latitude), float(longitude)

        # print(location, longitude, latitude)

        # Add the location to Redis
        r.geoadd(geo_key, (longitude, latitude, location))

print(f"\n\n Data added to Redis under the key '{geo_key}'. \n\n")

## Finding the Distance Between Two Cities
## Use GEODIST to find the distance between two cities in the dataset

distance = r.geodist("nj_cities", "Newark city", "Trenton city", unit="mi")
print(f"Distance between Newark and Trenton: {distance} mi \n\n")

## Querying Cities Within a Radius
## With GEORADIUS, you can find cities within a certain distance from a point.

cities_near_newark = r.geosearch(
    "nj_cities", "Newark city", radius=10, unit="mi", withdist=True
)
# print(cities_near_newark)
for city in cities_near_newark:
    print(f"{city[0]} is {city[1]} mi away from Newark")
