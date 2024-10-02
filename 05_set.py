from db_config import get_redis_connection

r = get_redis_connection()

# Deleting existing data
r.flushdb()

# Add followers to userID1's set
r.sadd("user:userID1:followers", "followerID1")
r.sadd("user:userID1:followers", "followerID2")

# Add followers to userID2's set
r.sadd("user:userID2:followers", "followerID1")
r.sadd("user:userID2:followers", "followerID3")

# Get all followers of userID1
all_followers_userID1 = r.smembers("user:userID1:followers")
print("\n All followers of userID1:", all_followers_userID1)

# Get all followers of userID2
all_followers_userID2 = r.smembers("user:userID2:followers")
print("\n All followers of userID2:", all_followers_userID2)

# Find common followers between userID1 and userID2
common_followers = r.sinter("user:userID1:followers", "user:userID2:followers")
print("\n Common followers:", common_followers)

# Get the number of followers of userID1
number_of_followers_userID1 = r.scard("user:userID1:followers")
print("\n Number of followers of userID1:", number_of_followers_userID1)

# Check if followerID1 is a follower of userID1
is_follower = r.sismember("user:userID1:followers", "followerID1")
print("\n Is followerID1 a follower of userID1:", is_follower)
