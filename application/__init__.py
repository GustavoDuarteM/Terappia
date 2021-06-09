from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_request_params import bind_request_params
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from datetime import datetime, timezone, timedelta
import redis

app = Flask(__name__)
app.config.from_object('config')
timezone(timedelta(hours=-3))

app.before_request(bind_request_params)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

bcrypt = Bcrypt(app)

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
jwt = JWTManager(app)
jwt_redis_blocklist = redis.StrictRedis(
  host="redis", port=6379, db=0, decode_responses=True
)
from application.controllers.helpers.session import *


from application.models import *
from application.controllers import *