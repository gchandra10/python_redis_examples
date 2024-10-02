from db_config import get_redis_connection

r = get_redis_connection()

# clear the memory
r.flushall()

# Adding cities
cities = [
    (-75.1118, 39.7029, 'Glassboro'),
    (-75.2241, 39.7393, 'MullicaHill'),
    (-75.3105, 39.7476, 'Swedesboro'),
    (-75.2404259, 39.8302, 'Paulsboro'),
    (-75.0246, 39.9268, 'CherryHill'),
    (-74.9489, 39.9689, 'Moorestown'),
]

restaurants = [
    (-75.11486, 39.72257, 'Italian Affiar Restaurant'),
    (-75.11275, 39.70404, 'LaScala Fire Glassboro'),
    (-75.11333, 39.70519, 'Mexican Mariachi Grill'),
]

pharmacies = [
    (-75.13068, 39.73228, 'Pitman Pharmacy'),
    (-75.09853, 39.68319, 'Walgreens Pharmacy'),
]

# GEOADD all cities,restaurants,pharmacies to their respective keys

for lon, lat, name in cities:
    r.geoadd('locations:cities', (lon, lat, name))

for lon, lat, name in restaurants:
    r.geoadd('locations:restaurant', (lon, lat, name))

for lon, lat, name in pharmacies:
    r.geoadd('locations:pharmacy', (lon, lat, name))

# Glassboro coordinates
latitude = 39.7029
longitude = -75.1118
radius = 2  # Radius in miles

# Query all nearby locations within 5 miles of Glassboro
nearby_locations = r.georadius('locations:cities', longitude, latitude, radius, unit='mi', withdist=True)
nearby_restaurants = r.georadius('locations:restaurant', longitude, latitude, radius, unit='mi', withdist=True)
nearby_pharmacies = r.georadius('locations:pharmacy', longitude, latitude, radius, unit='mi', withdist=True)

print(nearby_locations)
print(nearby_pharmacies)
print(nearby_restaurants)

# Combine results
combined_results = {
    'locations': nearby_locations,
    'restaurants': nearby_restaurants,
    'pharmacies': nearby_pharmacies
}

print(combined_results)

# Print the combined results
print("Nearby Locations within 2 miles of Glassboro:")
for category, results in combined_results.items():
    print(f"\n{category.capitalize()}:")
    for place in results:
        print(f"{place[0]} is {place[1]:.2f} miles away")
