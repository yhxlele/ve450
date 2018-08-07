import json
#import urllib.request
#from urllib.request import urlopen
import requests


url = "http://127.0.0.1:4000/sendfile"

values = {
    'input_dir': "wwwww",
    'output_dir': "ssss",
    'params': "zzzzzz"
}
with open("./Archive.zip") as f:
    req = requests.post(url, files={'file': f})
#try:
#    response = urlopen(req)
#    print(response.read())
#except urllib.error.HTTPError as e:
#    if e.code == 400:
#        context = {
#            "status": "HTTP Bad Request!"
#        }
#        return (flask.jsonify(**context), 400)
#    else:
#        context = {
#            "status": "HTTP Internal Error!"
#        }
#        return (flask.jsonify(**context), 500)
