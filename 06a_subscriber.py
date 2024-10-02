from db_config import get_redis_connection

# This subscribes to two channels

def listen_to_redis_channels():
    r = get_redis_connection()
    pubsub = r.pubsub()
    pubsub.subscribe(["class_update_channel", "school_update_channel"])

    for message in pubsub.listen():
        if message["type"] == "message":
            print(
                f"Received: {message.get('data')} on channel: {message.get('channel')}"
            )

if __name__ == "__main__":
    listen_to_redis_channels()
