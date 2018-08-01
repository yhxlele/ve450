from flask import Flask, request, g
from redis import Redis, RedisError
import importlib
import os
import socket
from threading import Thread
import time
from multiprocessing import Process
# import urllib
# import urllib.request
import urllib2
import requests
import tempfile
import zipfile
# from urllib.request import Request, urlopen
import flask
import json
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

UPLOAD_FOLDER = '/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

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
    context = {
        "name": "sendfile",
        "status": "fail"
    }

    if 'file' not in request.files:
        print("no file part")
        return (flask.jsonify(**context), 401)
    ref_file = request.files['file']
    
    
    if ref_file.filename == '':
        print('No selected file')
        return (flask.jsonify(**context), 402)

    request_json = flask.request.form.to_dict()
    print(request_json)
    # if ref_file and not zipfile.is_zipfile(ref_file.filename):
    #     print('Only zipfile allowed')
    #     return (flask.jsonify(**context), 403)
        
    context["status"] = "success"
    # /uploads/current_time/ref_file.filename()
    running_dir = os.path.join(app.config["UPLOAD_FOLDER"], str(time.time()))
    
    # create a folder for the running dir
    os.mkdir(running_dir)
    ref_file.save(os.path.join(running_dir, ref_file.filename))
    print(os.path.join(running_dir, ref_file.filename))
    if not zipfile.is_zipfile(os.path.join(running_dir, ref_file.filename)):
        return (flask.jsonify(**context), 401)
    
    zip_output = zipfile.ZipFile(os.path.join(running_dir, ref_file.filename))
    
    # all the files are in the running dir
    os.chdir(running_dir)
    zip_output.extractall()
    print(os.getcwd())

    thrd = Process(target=run_script, args=(str(request_json["command"]), ))
    g.running_thread = thrd
    thrd.start()
    return (flask.jsonify(**context), 201)
    # return (flask.jsonify(**context), 201)
    # data = request.get_json()
    # print("REQUEST = ", data)
    # input_file = data["input_dir"]
    # output_dir = data["output_dir"]

    # isValidPath, msg = checkpath(input_file, output_dir)

    # context = {
    #     "status": msg
    # }

    # if isValidPath:
    #     thrd = Process(target=run_python_file, args=(input_file, output_dir))
    #     g.running_thread = thrd
    #     thrd.start()
    #     return (flask.jsonify(**context), 201)

    # print("Message = ", msg)
    # return (flask.jsonify(**context), 400)

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


def run_script(cmd):
    # path, file = os.path.split(input_file)
    # os.chdir(path)
    
    # outputFileName = "stdout.txt"
    # os.system('python ' + os.path.join("/", input_file) + " > " + outputFileName)

    outputFileName = "_stdout.txt"
    os.system(cmd + " > " + outputFileName)
    url = "http://" + app.config["central_ip"] + ":8000/api/recvfile"
    with open(outputFileName) as f:
        req = requests.post(url, files={'file': f})


def register_container(url):
    local_ip = ""
    with open("/config.txt") as f:
        for line in f:
            local_ip = line.strip()

    print(local_ip)
    values = {
        'ip': local_ip,
        'container_id': '1',
        'container_name': 'Deep Learning Edge Node',
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
        "name": "gaole"
    }

    req = urllib2.Request("https://mboard-middle-server.herokuapp.com/api/getip", json.dumps(values).encode(encoding='UTF8'), headers={'Content-type':'application/json', 'Accept':'text/plain'})
    response = urllib2.urlopen(req)
    # print(json.loads(response.read()))
    tmp = json.loads(response.read())["ip"].strip()
    print(tmp)

    app.config["central_ip"] = tmp

    register_container("http://" + tmp + ":8000/api/register")
    app.run(host='0.0.0.0', port=80)


