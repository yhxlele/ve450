import json
import os
import urllib.request
from urllib.request import urlopen
from flask import render_template, request, redirect, url_for
import flask
import centralServer

@centralServer.app.route('/api/getInstanceData', methods=['GET'])
def getInstanceData():
    context = get_instance_data()
    # print(url)
    # print(json.dumps(values, indent=4, separators=(',', ': ')));
    # req = urllib.request.Request(url, json.dumps(values).encode(encoding='UTF8'), headers={'Content-type':'application/json', 'Accept':'text/plain'})
    # response = urlopen(req)
    # print(response.read())
    return (flask.jsonify(**context), 201)


def get_instance_data():
    org_data = []
    return_data = []
    with open(os.path.join('./centralServer', 'static/model/file.json'), "r") as f:
        line = f.readline()
        org_data = json.loads(line)
        for k, v in org_data.items():
            for kk, vv in v.items():
                return_data.append(vv)
    return {"data": return_data}
