import flask
# from flask.ext import shelve

app = flask.Flask(__name__)
app.config.from_object('centralServer.config')
app.config.from_envvar('SERVER_SETTINGS', silent=True)

# app.config['SHELVE_FILENAME'] = "shelve.db"
# shelve.init_app(app)

import centralServer.views
import centralServer.model
import centralServer.api