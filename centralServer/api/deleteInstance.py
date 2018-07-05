import json
import os
import urllib.request
from urllib.request import urlopen
from flask import render_template, request, redirect, url_for, g
import flask
import json
import centralServer
import struct, fcntl

@centralServer.app.route('/api/deleteInstance', methods=['POST'])
def deleteInstance():
    data = request.get_json()
    print(centralServer.app.instance_path)

    delete_instance(data)

    context = {
        "status" : "Delete an instance!"
    }

    return (flask.jsonify(**context), 201)


def delete_instance(data):
    ip_addr = data["ip"];

    with open(os.path.join('./centralServer', 'static/model/file.json'), "r+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)

        line = f.readline()
        org_data = json.loads(line)

        if ip_addr in org_data:
            org_data[ip_addr]["container_num"] -= 1
            if org_data[ip_addr]["container_num"] == 0:
                del org_data[ip_addr]
                pass

        f.seek(0)
        json.dump(org_data, f)
        fcntl.flock(f, fcntl.LOCK_UN)
