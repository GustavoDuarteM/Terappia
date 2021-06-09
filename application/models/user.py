from application.models.base import Base
from application import bcrypt
from application import db 

class User(Base):
  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)
  password_hash = db.Column(db.LargeBinary, nullable=False)
  phone = db.Column(db.String, nullable=False)

  def __init__(self, name, email, password, phone):
    self.name = name
    self.email = email
    self.password_hash = bcrypt.generate_password_hash(password)
    self.phone = phone

  def check_password(self, password):
    return bcrypt.check_password_hash(self.password_hash, password)