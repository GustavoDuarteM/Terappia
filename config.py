from os import environ 
import re

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL').replace("postgres","postgresql")
SQLALCHEMY_TRACK_MODIFICATIONS = True
JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
if 'REDIS_URL' in environ:
  REDIS_HOST = re.split('[\: :@]',environ.get('REDIS_URL'))[3]
  REDIS_PASSWORD = re.split('[\: :@]',environ.get('REDIS_URL'))[2]
  REDIS_PORT = re.split('[\: :@]',environ.get('REDIS_URL'))[-1]
else:
  REDIS_HOST = environ.get('REDIS_HOST')
  REDIS_PORT = environ.get('REDIS_PORT')
  REDIS_PASSWORD = environ.get('REDIS_PASSWORD')
