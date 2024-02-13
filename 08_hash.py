import pandas as pd

from db_config import get_redis_connection

r = get_redis_connection()

# Example hash key and field-value pairs
hash_key = 'product:100'
product_details = {
    'name': 'Smartphone',
    'price': '699.99',
    'stock': '50'
}

# Use hset with mapping to set multiple fields at once
# Efficent for bulk updates because it reduces the round trip to Redis Server
r.hset(hash_key, mapping=product_details)

