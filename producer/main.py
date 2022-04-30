from time import sleep
import redis

def getRedisClient() -> Redis:
    """
    Function used to get a Redis Client
    
    Returns:
        Redis: The instance of the Redis connection
    """
    
    return redis.Redis(host="redis_pub_sub", port=6379)

def main():
    client = getRedisClient()

    while True:
        sleep(2)
        print("Publishing \"Hello world\" to channel \"test\"")

        # Uses the Redis connection to publish the message "Hello World" to the
        # channel "test"
        client.publish("test", "Hello World")

if __name__ == "__main__":
    main()