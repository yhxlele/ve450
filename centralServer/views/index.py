import json
import urllib.request
from urllib.request import urlopen
from flask import render_template, request, redirect, url_for
import centralServer

@centralServer.app.route('/', methods=['GET'])
def show_index():
    # deprecated!!!
	context = {'css': url_for('static', filename = 'css/style.css')}
	# if request.method == 'POST':
	# 	data = request.form
	# 	if 'form_in' in data:
	# 		text = data['text']
	# 		url = "http://127.0.0.1:80/sendfile"
	# 		values = {'dir': text}
	# 		print(url)
	# 		print(json.dumps(values, indent=4, separators=(',', ': ')));
	# 		req = urllib.request.Request(url, json.dumps(values).encode(encoding='UTF8'), headers={'Content-type':'application/json', 'Accept':'text/plain'})
	# 		response = urlopen(req)
	# 		print(response.read())
	return render_template('index.html', **context)



# @centralServer.app.route('/', methods=['GET'])
# def show_index():
# 	context = {'css': url_for('static', filename = 'css/style.css')}
# 	if request.method == 'POST':
# 		data = request.form
# 		if 'form_in' in data:
# 			text = data['text']
# 			url = "http://127.0.0.1:80/sendfile"
# 			values = {'dir': text}
# 			print(url)
# 			print(json.dumps(values, indent=4, separators=(',', ': ')));
# 			req = urllib.request.Request(url, json.dumps(values).encode(encoding='UTF8'), headers={'Content-type':'application/json', 'Accept':'text/plain'})
# 			response = urlopen(req)
# 			print(response.read())
# 	return render_template('index.html', **context)




