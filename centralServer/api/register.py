import json
import os
import urllib.request
from urllib.request import urlopen
from flask import render_template, request, redirect, url_for, g
import flask
import json
import centralServer
import struct, fcntl
import socket



@centralServer.app.before_first_request
def set_up():
    g.data = []
    with open(os.path.join('./centralServer', 'static/model/file.json'), "w") as f:
        f.write("{}")
    
    # local_ip = socket.gethostbyname(socket.gethostname())
    # values = {
    #     "name": "brad",
    #     "ip": local_ip
    # }
    # req = urllib.request.Request("http://localhost:8080/api/sendip", json.dumps(values).encode(encoding='UTF8'), headers={'Content-type':'application/json', 'Accept':'text/plain'})
    # response = urlopen(req)
    # print(response.read())



@centralServer.app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()

    add_new_instance(data, request.remote_addr)

    context = {
        "status": "new instance added!"
    }
    return (flask.jsonify(**context), 201)


def add_new_instance(data, ip_addr):
    org_data = []
    with open(os.path.join('./centralServer', 'static/model/file.json'), "r+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        line = f.readline()
        org_data = json.loads(line)
        ip_addr = data["ip"]
        print(data)
        print(ip_addr)
        if ip_addr not in org_data:
            org_data[ip_addr] = data
            org_data[ip_addr]["container_num"] = 1
            # org_data[ip_addr]["ip"] = ip_addr
            pass
        else:
            org_data[ip_addr]["container_num"] += 1
            pass

        # container_id = data["container_id"]
        # print(org_data)
        # if container_id in org_data:
        #     org_data[container_id]["container_num"] += 1
        #     pass
        # else:
        #     org_data[container_id] = data
        #     org_data[container_id]["container_num"] = 1
        #     pass
        f.seek(0)
        json.dump(org_data, f)
        fcntl.flock(f, fcntl.LOCK_UN)
