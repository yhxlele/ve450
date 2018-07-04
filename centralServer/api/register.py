import json
import os
import urllib.request
from urllib.request import urlopen
from flask import render_template, request, redirect, url_for, g
import flask
import json
import centralServer
import struct, fcntl



@centralServer.app.before_first_request
def set_up():
    g.data = []
    with open(os.path.join('./centralServer', 'static/model/file.json'), "w") as f:
        f.write("{}")


@centralServer.app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    print(centralServer.app.instance_path)

    add_new_instance(data)

    context = {
        "status": "new instance added!"
    }
    return (flask.jsonify(**context), 201)


def add_new_instance(data):
    org_data = []
    with open(os.path.join('./centralServer', 'static/model/file.json'), "r+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        line = f.readline()
        org_data = json.loads(line)
        
        container_id = data["container_id"]
        print(org_data)
        if container_id in org_data:
            org_data[container_id]["container_num"] += 1
            pass
        else:
            org_data[container_id] = data
            org_data[container_id]["container_num"] = 1
            pass
        f.seek(0)
        json.dump(org_data, f)
        fcntl.flock(f, fcntl.LOCK_UN)
