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
    print("REQUEST = ", data)
    input_file = data["input_dir"]
    output_dir = data["output_dir"]

    isValidPath, msg = checkpath(input_file, output_dir)

    context = {
        "status": msg
    }

    if isValidPath:
        thrd = Process(target=run_python_file, args=(input_file, output_dir))
        g.running_thread = thrd
        thrd.start()
        return (flask.jsonify(**context), 201)

    print("Message = ", msg)
    return (flask.jsonify(**context), 400)

def checkpath(input_file, output_dir):
    valid = 0
    if os.path.isfile(input_file):
        valid += 1
    if os.path.exists(output_dir):
        valid += 3

    if valid == 1:
        return False, "Invalid output directory!"
    elif valid == 3:
        return False, "Invalid input file path and name!"
    elif valid == 0:
        return False, "Invalid two file paths!"
    else:
        return True, "Valid file paths."


@app.route("/stopthread", methods=['GET'])
def stopthread():
    g.running_thread.terminate()


def run_python_file(input_file, output_dir):
    path, file = os.path.split(input_file)
    os.chdir(path)
    
    outputFileName = "stdout.txt"
    os.system('python ' + os.path.join("/", input_file) + " > " + outputFileName)


def register_container(url):
    local_ip = ""
    with open("/config.txt") as f:
        for line in f:
            local_ip = line

    print(local_ip)
    values = {
        'ip': local_ip,
        'container_id': '2',
        'container_name': 'Deep Learning Container',
        'description': 'Input python script path to train model',
        'input_list_label': ['Python Script Path', 'Output Path', 'Parameter lists'],
        'request_list_label': ['input_dir', 'output_dir', 'params']
    }

    print(values)
    req = urllib2.Request(url, json.dumps(values).encode(encoding='UTF8'), headers={'Content-type':'application/json', 'Accept':'text/plain'})
    
    try:
        response = urllib2.urlopen(req)
        print(response.read())
    except:
        print("register stage error!")
    # print(response.read())


if __name__ == "__main__":    
    values = {
        'method': "get_ip",
        "name": "brad"
    }

    req = urllib2.Request("https://mboard-middle-server.herokuapp.com/api/getip", json.dumps(values).encode(encoding='UTF8'), headers={'Content-type':'application/json', 'Accept':'text/plain'})
    response = urllib2.urlopen(req)
    # print(json.loads(response.read()))
    tmp = json.loads(response.read())["ip"]
    print(tmp)
    register_container("http://" + tmp + ":8000/api/register")
    app.run(host='0.0.0.0', port=80)


