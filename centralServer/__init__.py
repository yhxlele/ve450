import flask

app = flask.Flask(__name__)
app.config.from_object('centralServer.config')

import centralServer.views
import centralServer.model