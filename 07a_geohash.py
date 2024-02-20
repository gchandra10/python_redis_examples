# pip3 install python-geohash
import geohash

# Encode a location
latitude = 40.689247
longitude = -74.044502
precision = 12  # More digits = more precision
encoded = geohash.encode(latitude, longitude, precision)
print(f"Encoded: {encoded}")

# Decode a GeoHash
decoded = geohash.decode(encoded)
print(f"Decoded: {decoded}")
