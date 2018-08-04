import json
import urllib.request
from urllib.request import urlopen
from flask import render_template, request, redirect, url_for
import flask
import centralServer
import os

@centralServer.app.route('/api/recvfile', methods=['POST'])
def recvfile():
    
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
        
    context["status"] = "success"
    request_json = flask.request.form.to_dict()
    root_dir = os.path.join('./centralServer', 'static/result' + '/' + request_json["ip"] + "#" + request_json["container_id"])
    print(root_dir)
    # create a folder to store the final _stdout
    result_dir = root_dir
    print(result_dir)
    # if not exists, create the folder
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    
    # save the file
    ref_file.save(os.path.join(result_dir, ref_file.filename))
    # os.chdir(running_dir)
    # print(os.getcwd())
    # print(os.listdir(os.getcwd()))
    
    # print("recvfile succeed")
    return (flask.jsonify(**context), 201)