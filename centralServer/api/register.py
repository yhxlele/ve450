import json
import os
import urllib.request
from urllib.request import urlopen
from flask import render_template, request, redirect, url_for, g
import flask
import json
import centralServer


@centralServer.app.before_first_request
def set_up():
    g.data = []
    print()


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
    with open(os.path.join('./centralServer', 'static/model/file.json'), "r") as f:
        line = f.readline()
        org_data = json.loads(line)
    org_data.append(data)

    print(len(org_data))
    with open(os.path.join('./centralServer', 'static/model/file.json'), "w") as f:
        json.dump(org_data, f)
    


