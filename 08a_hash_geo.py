from db_config import get_redis_connection
r = get_redis_connection()

# Adding geospatial locations for restaurants
restaurants = [
    (-75.11486, 39.72257, 'Italian Affiar Restaurant'),
    (-75.11275, 39.70404, 'LaScala Fire Glassboro'),
    (-75.11333, 39.70519, 'Mexican Mariachi Grill'),
]

# Add geospatial data for restaurants
for lon, lat, name in restaurants:
    r.geoadd('locations:restaurant', (lon, lat, name))

# Store metadata for each restaurant using Redis hashes
restaurant_metadata = {
    'Italian Affiar Restaurant': {"name": "Italian Affair", "menu": "Pasta, Pizza", "rating": "4.5", "contact": "555-1234"},
    'LaScala Fire Glassboro': {"name": "LaScala Fire", "menu": "Pizza, Grill", "rating": "4.7", "contact": "555-5678"},
    'Mexican Mariachi Grill': {"name": "Mariachi Grill", "menu": "Tacos, Burritos", "rating": "4.2", "contact": "555-9876"},
}

# Use hset with mapping to store metadata
for restaurant, details in restaurant_metadata.items():
    r.hset(f"restaurant:{restaurant}", mapping=details)

# Glassboro coordinates
latitude = 39.7029
longitude = -75.1118
radius = 1  # radius in miles

# Query nearby restaurants within 5 miles of Glassboro
nearby_restaurants = r.georadius('locations:restaurant', longitude, latitude, radius, unit='mi', withdist=True)

print(nearby_restaurants)

# Print the nearby restaurants along with their metadata
print("Nearby Restaurants with more details:")
for place in nearby_restaurants:
    restaurant_name = place[0]
    distance = place[1]
    metadata = r.hgetall(f"restaurant:{restaurant_name}")
    
    metadata = {k: v for k, v in metadata.items()}
    
    # Display the result
    print(f"\nRestaurant: {restaurant_name}")
    print(f"  Distance: {distance:.2f} miles")
    print(f"  Name: {metadata.get('name')}")
    print(f"  Menu: {metadata.get('menu')}")
    print(f"  Rating: {metadata.get('rating')}")
    print(f"  Contact: {metadata.get('contact')}")
