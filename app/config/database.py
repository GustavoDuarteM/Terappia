from application import app
from flask_sqlalchemy import SQLAlchemy

POSTGRES = {
  'user': 'terapia_app',
  'pw': 'a123456',
  'db': 'terapia_app',
  'host': 'localhost',
  'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db = SQLAlchemy(app)