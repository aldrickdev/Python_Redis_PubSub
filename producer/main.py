from time import sleep
import redis

def getRedisClient():
    return redis.Redis(host="redis_pub_sub", port=6379)

def main():
    client = getRedisClient()

    while True:
        sleep(2)
        print("Publishing \"Hello world\" to channel \"test\"")
        client.publish("test", "Hello World")

if __name__ == "__main__":
    main()