from app import db 
import inspect

class Base(db.Model):
  __abstract__ = True

  # def attributes():
  #   for attr in inspect.getmembers(User):
  #       if not attr[0].startswith('_'):
  #         if not inspect.ismethod(attr[1]):
  #           print(attr)
    # if not i[0].startswith('_'):