from app.models.base import Base
from app import db 

class User(Base):
  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)
  password = db.Column(db.String, nullable=False)
  phone = db.Column(db.String, nullable=False)

  def __init__(self, name, email, password, phone):
    self.name = name
    self.email = email
    self.password = password
    self.phone = phone