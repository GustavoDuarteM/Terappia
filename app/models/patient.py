from app.models.base import Base
from app import db
from app.models.user import User

class Patient(Base):
  __tablename__ = "patients"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  email = db.Column(db.String, nullable=False)
  phone = db.Column(db.String, nullable=False)

  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  user = db.relationship('User',backref=db.backref('patients', lazy=True))

  def __init__(self, name, email, phone, user_id):
    self.name = name
    self.email = email
    self.phone = phone
    self.user_id = user_id