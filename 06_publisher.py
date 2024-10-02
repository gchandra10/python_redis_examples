import sys
from db_config import get_redis_connection

# Redis Pub/Sub is transient: if no subscriber is present at the
# moment a message is published, the message is lost.
# For persistent messaging, consider other Redis data structures like lists.

def publish_message(channel, message):
    """Publishes a message to a specified Redis channel."""
    r = get_redis_connection()
    r.publish(channel, message)
    print(f"Published message to {channel}: {message}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python publisher.py <channel> <message>")
        sys.exit(1)

    channel = sys.argv[1]
    message = sys.argv[2]

    publish_message(channel, message)

    # poetry run python 06_publisher.py 'class_update_channel', 'Hello class'
    # poetry run python 06_publisher.py 'school_update_channel', 'who is graduating this summer?'
    # poetry run python 06_publisher.py 'glassboro_channel', 'welcome to Glassboro'