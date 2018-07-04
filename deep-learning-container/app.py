from flask import Flask, request, g
from redis import Redis, RedisError
import importlib
import os
import socket
from threading import Thread
from multiprocessing import Process
# import urllib
# import urllib.request
import urllib2
# from urllib.request import Request, urlopen
import flask
import json

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
    dir_data = data["input_dir"]
    thrd = Process(target=run_python_file, args=(dir_data, ))
    g.running_thread = thrd
    thrd.start()
    return "succeed in sending running script"


@app.route("/stopthread", methods=['GET'])
def stopthread():
    g.running_thread.terminate()


def run_python_file(dir):
    os.system('python ' + os.path.join("/", dir))


def register_container(url):
    
    local_ip = socket.gethostbyname(socket.gethostname())
    print(local_ip)
    values = {
        'ip': local_ip,
        'container_id': '1',
        'container_name': 'Deep Learning Container',
        'description': 'Input python script path to train model',
        'input_list_label': ['Python Script Path', 'Output Path', 'Parameter lists'],
        'request_list_label': ['input_dir', 'output_dir', 'params']
    }

    print(values)
    req = urllib2.Request(url, json.dumps(values).encode(encoding='UTF8'), headers={'Content-type':'application/json', 'Accept':'text/plain'})
    response = urllib2.urlopen(req)
    print(response.read())


if __name__ == "__main__":
    register_container("http://192.168.1.102:8000/api/register")
    app.run(host='0.0.0.0', port=80)


