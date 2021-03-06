from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
api = Api(app)
db = SQLAlchemy(app)

from app.views import index

from app.resources.shorten import Shorten
from app.resources.goto import Goto

api.add_resource(Shorten, '/')
api.add_resource(Goto, '/<short_hash>')
