from db_config import get_redis_connection

def listen_to_redis_patterns():
    r = get_redis_connection()
    pubsub = r.pubsub()
    pubsub.psubscribe('*_channel')
    pubsub.subscribe(['bg_class_mates'])
    
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Received: {message.get('data')} on channel: {message.get('channel')}")
        elif message['type'] == 'pmessage':
            print(f"Pattern Received: {message.get('data')} on channel: {message.get('channel')}")

if __name__ == "__main__":
    listen_to_redis_patterns()