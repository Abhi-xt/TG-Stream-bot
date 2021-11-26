import requests
import time
from threading import Thread

def ping_app():
    while True:
        requests.get("https://streamxt.herokuapp.com")
        time.sleep(120)

t = Thread(target=ping_app)
t.start()
