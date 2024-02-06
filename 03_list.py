from db_config import get_redis_connection
r = get_redis_connection()

r.flushall()

# LPUSH commands
r.lpush("user:123:recentPages", "/home")
r.lpush("user:123:recentPages", "/contact")

# RPUSH command
r.rpush("user:123:recentPages", "/services")

# LRANGE command to get all pages
pages = r.lrange("user:123:recentPages", 0, -1)
print("Pages after LPUSH and RPUSH:", pages)

# LLEN command to get the length of the list
length = r.llen("user:123:recentPages")
print("Number of pages:", length)

# LPOP command to remove and return the first element
removed_page = r.lpop("user:123:recentPages")
print("Removed page:", removed_page)

# LRANGE command to get all pages after LPOP
pages_after_lpop = r.lrange("user:123:recentPages", 0, -1)
print("Pages after LPOP:", pages_after_lpop)