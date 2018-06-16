import flask

app = flask.Flask(__name__)
app.config.from_object('centralServer.config')
app.config.from_envvar('SERVER_SETTINGS', silent=True)


import centralServer.views
import centralServer.model