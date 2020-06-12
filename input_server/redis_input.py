import redis
import time
import json
import random


if __name__ == "__main__":
    redis_server = redis.Redis(host='localhost', port=6379, db=0)

    channel_name = "my_channel"

    while True:
        timestamp =int ( time.time())
        total_count = random.randint(5,15)
        value_a = random.randint(1,5)
        value_b = total_count - value_a
        data = {"timestamp" : timestamp,
            "metrics":{
                "total":total_count,
                "a":value_a,
                "b":value_b
            }
        }
        json_data = json.dumps(data)

        redis_server.publish(channel_name,json_data)

        print("message sent -> message = {}".format(json_data))

        time.sleep(2)