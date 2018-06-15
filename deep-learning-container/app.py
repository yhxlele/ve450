from flask import Flask, request, g
from redis import Redis, RedisError
import importlib
import os
import socket
from threading import Thread
from multiprocessing import Process

redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)


@app.route("/")
def main():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"
    
    # "/Users/menggaole/Desktop/Untitled/app.py"

    html = "<h3> Running {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)


@app.route("/sendfile", methods=['POST'])
def sendfile():
    data = request.get_json()
    print(data)
    dir_data = data["dir"]
    thrd = Process(target=run_python_file, args=(dir_data, ))
    g.running_thread = thrd
    thrd.start()
    return "succeed in sending running script"


@app.route("/stopthread", methods=['GET'])
def stopthread():
    g.running_thread.terminate()


def run_python_file(dir):
    os.system('python /sharedfolder' + dir)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
