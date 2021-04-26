from app import db 
from flask_sqlalchemy import inspect

class Base(db.Model):
  __abstract__ = True

  # def attributes():
  #   for attr in inspect.getmembers(User):
  #       if not attr[0].startswith('_'):
  #         if not inspect.ismethod(attr[1]):
  #           print(attr)
    # if not i[0].startswith('_'):
  
  def save(self):
    try:
      db.session.add(self)
      db.session.commit()
      return True
    except:
      print('houve uma falha em salvar')
      return False

  def delete(self):
    try:
      db.session.delete(self)
      db.session.commit()
    except:
      print('houve uma falha em remover')
  
  def serialize(self):
    return {attr: getattr(self, attr) for attr in inspect(self).attrs.keys()}