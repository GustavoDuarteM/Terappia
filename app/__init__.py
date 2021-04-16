from config.database import db 
from config.application import app
from controllers import *

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)