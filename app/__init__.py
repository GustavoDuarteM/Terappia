from application import app
from config import manager
from controllers import *

if __name__ == '__main__':
    manager.run()
    app.run('0.0.0.0', port=8080)