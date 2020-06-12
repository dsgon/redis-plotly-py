# redis-plotly-py
Redis Edge integration with Plotly using Python

## Getting Started

This project is a simple demo to know how to integrate a module Server with a module Visualization using Topics on Redis.


### Prerequisites

> - [Python](https://www.python.org/downloads/)
> - [docker](https://www.docker.com/)
> - It is usually good to work in a virtualenv or venv to avoid conflicts with other package managers and Python projects. [python virtual environment](https://docs.python.org/3/tutorial/venv.html) (Optional)

### Installing

> #### Requirements
> - You need install module/libs from *requirements.txt* file
> ```
> $ pip install -r requirements.txt
> ```

### Settings
> #### Run docker Redis Service
> To run this example you must have Docker Service running. 
> The first step is to build and run the Redis Server. Redis works on the port **6379** by default, so you can create an image with a tag and then run it. Remember to expose the Redis port on the image docker
> ```
> $ docker build <path_to_dockerfile> -t <you_tag>
> ```
> ```
> $ docker run -d -p 0.0.0.0:6379:6379 <you_tag>
> ```
> to get more info, you can visit [redis dockerhub](https://hub.docker.com/r/redislabs/redisedge)

> #### Run Input Server
> This is a python file that works as generator data. In this demo, it creates a JSON message, and sets a Topic on Redis sending a new message every 2 seconds.
> To execute this file you only should call the python file.
> ```
> $ python redis_input.py
> ```
> The output will be like this:
> ```
> message sent -> message = {"timestamp": 1591937508, "metrics": {"total": 6, "a": 5, "b": 1}}
> ```

> #### Run Visualization Server
> This is a python file that uses Plotly Dash to draw the data that has been get from Redis Topic. Remember this: to get messages from a Topic you must subscribe first. 
> In this demo this file gets the JSON message and draws the data every second. The Frontend is autorefresh because it uses a callback from Flask that it's generated by Plotly interval. This file has been configured to run on **localhost** on the port **8050**

> To execute this file you only call the python file.
> ```
> $ python visualization_server.py
> ```
> Now you can go to the browser a check you data generated and it's done! You have a Redis Service handling messages from a topic generated by the Input service and consumed by the Visualization Services, and these messages are draw with Plotly.


## Authors

* **David Gonzalez** - *Initial work* - [github](https://github.com/dsgon/) - [twitter](https://twitter.com/__dsgon)


## Reference Links
> [Plotly](https://plotly.com/python/)
> [Redis](https://redis.io/documentation)
> [pip redis](https://pypi.org/project/redis/)




