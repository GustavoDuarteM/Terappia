from app.models.base import Base
from app import db, datetime
from app.models.user import User
from app.models.patient import Patient

class Session(Base):
  __tablename__ = "sessions"

  id = db.Column(db.Integer, primary_key=True)
  start = db.Column(db.DateTime, nullable=False)
  end = db.Column(db.DateTime, nullable=False)

  patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
  patient = db.relationship('Patient',backref=db.backref('sessions', lazy=True))

  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  user = db.relationship('User',backref=db.backref('sessions', lazy=True))

  def __init__(self, start, end, patient, user):
    self.start =  start
    self.end = end
    self.patient = patient
    self.user = user