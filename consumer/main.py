from time import sleep
import redis


def getRedisClient():
    return redis.Redis(host="redis_pub_sub", port=6379)


def checkForMessage(pubsub :redis.client.PubSub) -> str | None:
    message = pubsub.get_message()

    if message:
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
    pubsub.subscribe("test")

    while True:
        message = checkForMessage(pubsub)

        if message is not None:
            print(message)


if __name__ == "__main__":
    main()