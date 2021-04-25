from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_request_params import bind_request_params

app = Flask(__name__)
app.config.from_object('config')

app.before_request(bind_request_params)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.models import *
from app.controllers import *