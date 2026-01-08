#script creates web server that counts how many times the 
#page has been visited

import time
import redis
from flask import Flask

app = Flask(__name__)

# Connect to Redis (the hostname 'redis' comes from docker-compose)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f"<h1>Weather Dashboard</h1><p>This page has been viewed {count} times.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)