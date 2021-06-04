from app import db, datetime
from flask_sqlalchemy import inspect

class Base(db.Model):
  __abstract__ = True
  
  create_at = db.Column(db.DateTime, default=datetime.now, nullable=False)

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
  
  def serialize(self, attr_remove=[]):
    attrs = inspect(self).attrs.keys()
    return {attr: getattr(self, attr) for attr in attrs if not attr in attr_remove}
  
  def setattrs(_self, **kwargs):
    for k,v in kwargs.items():
        setattr(_self, k, v)