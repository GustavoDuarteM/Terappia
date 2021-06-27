from application import db, datetime
from flask_sqlalchemy import inspect
from enum import Enum

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
      return True
    except:
      print('houve uma falha em remover')
      return False
  
  def serialize(self, attr_remove=[]):
    attr_remove.append('create_at')
    attrs = inspect(self).attrs.keys()
    result = {}
    for attr in attrs:
      val = getattr(self, attr)
      if not attr in attr_remove and not issubclass(type(val), Base):
        if isinstance(val, Enum):
          result.update({attr: val.value})
        else:
          result.update({attr: val})

    return result

  def setattrs(_self, **kwargs):
    for k,v in kwargs.items():
        setattr(_self, k, v)