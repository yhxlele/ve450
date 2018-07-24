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
    running_dir = os.path.join('./centralServer', 'static/model')
    
    # create a folder for the running dir
    ref_file.save(os.path.join(running_dir, ref_file.filename))
    print(os.path.join(running_dir, ref_file.filename))
    os.chdir(running_dir)
    print(os.getcwd())
    print(os.listdir(os.getcwd()))
    
    print("recvfile succeed")
    return (flask.jsonify(**context), 201)