from application.models.base import Base
from application import db, datetime
from application.models.user import User
from application.models.patient import Patient
from application.models.enums.session_status import StatusSessionEnum

class Session(Base):
  __tablename__ = "sessions"

  id = db.Column(db.Integer, primary_key=True)
  start = db.Column(db.DateTime, nullable=False)
  end = db.Column(db.DateTime, nullable=False)
  comments = db.Column(db.String, default = "")
  status = db.Column(db.Enum(StatusSessionEnum), default = StatusSessionEnum.PENDING, nullable=False)

  patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
  patient = db.relationship('Patient',backref=db.backref('sessions', lazy=True))

  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  user = db.relationship('User',backref=db.backref('sessions', lazy=True))

  def __init__(self, start, end, patient_id, user_id):
    # datetime.strptime('2021-03-07 03:22', "%Y-%m-%d %H:%M")
    self.start =  datetime.strptime(start, "%Y-%m-%d %H:%M")
    self.end = datetime.strptime(end, "%Y-%m-%d %H:%M") 
    self.patient_id = patient_id 
    self.user_id = user_id

  def valid(self):
    if self.start >= self.end : return False
    try:
      sessions = Session.query.filter_by(user_id= self.user_id)
      if sessions.count() == 0 : return True
      sessions = sessions.filter( Session.id != self.id )
      sessions = sessions.filter( 
        ((Session.start >= self.start) & (Session.start <= self.end)) 
        |  ((Session.end >= self.start) & (Session.end <= self.end))
      )
      return sessions.count() < 1
    except:
      return False