import json
import urllib.request
from urllib.request import urlopen
from flask import render_template, request, redirect, url_for
import flask
import centralServer
import requests

@centralServer.app.route('/api/sendtask', methods=['POST'])
def sendtask():
    
    # values = {'dir':}
    print("data ", flask.request.data)
    print(flask.request.form.to_dict())
    request_json = flask.request.form.to_dict()
    # print(request_json)
    # job_name = request_json["job"]
    
    url = "http://" + request_json["ip"] + ":4000/sendfile"

    # values = {
    #     'input_dir': request_json["input_dir"],
    #     'output_dir': request_json["output_dir"],
    #     'params': request_json["params"]
    #}
    # req = urllib.request.Request(url, json.dumps(values).encode(encoding='UTF8'), headers={'Content-type':'application/json', 'Accept':'text/plain'})
    try:
        requests.post(url, files={'file': request.files['file']})
    except urllib.error.HTTPError as e:
        if e.code == 400:
            context = {
                "status": "HTTP Bad Request!"
            }
            return (flask.jsonify(**context), 400)
        else:
            context = {
                "status": "HTTP Internal Error!"
            }
            return (flask.jsonify(**context), 500)
        
    context = {
        "status": "Succeed!"
    }
    # print(url)
    # print(json.dumps(values, indent=4, separators=(',', ': ')));
    # req = urllib.request.Request(url, json.dumps(values).encode(encoding='UTF8'), headers={'Content-type':'application/json', 'Accept':'text/plain'})
    # response = urlopen(req)
    # print(response.read())
    return (flask.jsonify(**context), 201)





