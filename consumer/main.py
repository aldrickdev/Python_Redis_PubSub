from time import sleep
import redis


def getRedisClient():
    """
    Function used to get a Redis Client
    
    Returns:
        Redis: The instance of the Redis connection
    """

    return redis.Redis(host="redis_pub_sub", port=6379)


def checkForMessage(pubsub :redis.client.PubSub) -> str | None:
    """This function will use the provided PubSub client to check if a message
     has been published in the subscribed channel

    Args:
        pubsub (redis.client.PubSub): The PubSub client

    Returns:
        str | None: If a message has been published then return it, if not 
        return None
    """
    message = pubsub.get_message()

    if message:
        # extracts the data from the message
        data = message.get('data')

        # Data was published by the producer, lets return it
        if data != 1:
            return data.decode('utf-8')

        # Successful subscription message
        channel = message.get('channel').decode('utf-8')

        print(f"Successfully Subcribed to {channel}")
    
    return None


def main():
    client = getRedisClient()
    pubsub = client.pubsub()
    
    # Subscribes to the "test" channel
    pubsub.subscribe("test")

    while True:
        message = checkForMessage(pubsub)

        if message is not None:
            print(message)


if __name__ == "__main__":
    main()