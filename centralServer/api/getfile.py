import json
import urllib.request
from urllib.request import urlopen
from flask import render_template, request, redirect, url_for
import flask
import centralServer
import os

@centralServer.app.route('/api/getfile', methods=['GET'])
def getfile():
    context = {
        "name": "sendfile",
        "status": "fail",
        "file_list": []
    }

    context["status"] = "success"
    request_json = flask.request.form.to_dict()
    root_dir = os.path.join('./centralServer', 'static/result')
    
    # 10.167.172.56.1
    # list of {"container_id": , "ip": , "file_content": }
    for subdir in os.listdir(root_dir):
        
        tmp = os.path.join(root_dir, subdir)

        output_file_path = os.path.join(tmp, "_stdout.txt")
        if os.path.isfile(output_file_path):
            with open(output_file_path, "r") as f:
                edge_ip, container_id = subdir.split('#', 1)
                context["file_list"].append({
                    "container_id": container_id,
                    "edge_ip": edge_ip,
                    "file_content": f.read()
                })

    return (flask.jsonify(**context), 201)
