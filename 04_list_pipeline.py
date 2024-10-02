# Execute set of commands as one block

from db_config import get_redis_connection

r = get_redis_connection()

r.flushall()

# Create a pipeline
pipe = r.pipeline()

# LPUSH commands
pipe.lpush("user:123:recentPages", "/home")
pipe.lpush("user:123:recentPages", "/contact")

# RPUSH command
pipe.rpush("user:123:recentPages", "/services")

# LRANGE command to get all pages (queued, not executed yet)
pipe.lrange("user:123:recentPages", 0, -1)

# LLEN command to get the length of the list (queued, not executed yet)
pipe.llen("user:123:recentPages")

# LPOP command to remove and return the first element (queued, not executed yet)
pipe.lpop("user:123:recentPages")

# LRANGE command to get all pages after LPOP (queued, not executed yet)
pipe.lrange("user:123:recentPages", 0, -1)

# Execute all commands in the pipeline at once
responses = pipe.execute()

print(responses)

# # responses[0] contains the result of the first LRANGE
# print("Pages after LPUSH and RPUSH:", responses[3])

# # responses[1] contains the result of LLEN
# print("Number of pages:", responses[4])

# # responses[2] contains the result of LPOP
# print("Removed page:", responses[5])

# # responses[3] contains the result of the second LRANGE (after LPOP)
# print("Pages after LPOP:", responses[6])
