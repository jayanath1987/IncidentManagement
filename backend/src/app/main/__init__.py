from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS, cross_origin
from ..main.middleware.authorization import Authorizer
from .config import config_by_name

UPLOAD_FOLDER = '/files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.wsgi_app = Authorizer(app.wsgi_app)
CORS(app)
blueprint = Blueprint('api', __name__)
api = Api(blueprint)
app.register_blueprint(blueprint)

db = SQLAlchemy()

def create_app(config_name):
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    
    return app

def instancePath():
    return app.instance_path

def rootPath():
    print (app.root_path)
    return app.root_path

def projectRoot():
    print ((app.root_path[:-9]))
    return (app.root_path[:-9])
