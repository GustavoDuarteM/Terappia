from flask import request, jsonify
from app import app, datetime
from app.models.session import Session
from app.models.patient import Patient
from flask_jwt_extended import jwt_required, current_user

@app.route('/sessions', methods=['POST'])
@jwt_required()
def new_sessions():
  params = session_params()
  patient = Patient.query.filter_by(id = params['patient_id'], user_id = current_user.id).first()
  if not patient : return invalid_session()
  session = Session(**session_params(), user_id = current_user.id )
  if session.save():
      return jsonify(session = session.serialize(['user','patient']))
  else:
    return invalid_session()

@app.route('/sessions/<int:id>', methods=['GET'])
@jwt_required()
def show_sessions(id):
  session = Session.query.filter_by(id = id, user_id = current_user.id).first()
  if session:
      return jsonify(session = session.serialize(['user','patient']))
  else:
    return invalid_session()

@app.route('/sessions', methods=['PUT'])
@jwt_required()
def edit_sessions():
  params = session_params()
  session = Session.query.filter_by(id = params['id'], user_id = current_user.id).first()
  patient = Patient.query.filter_by(id = params['patient_id'], user_id = current_user.id).first()
  if (not session) or (not patient): return invalid_session() 
  if params['start'] : session.start =  datetime.strptime(params['start'], "%Y-%m-%d %H:%M")
  if params['end'] : session.end = datetime.strptime(params['end'], "%Y-%m-%d %H:%M") 
  session.patient = patient
  if session.save():
      return jsonify(session = session.serialize(['user','patient']))
  else:
    return invalid_session()

@app.route('/sessions', methods=['GET'])
@jwt_required()
def all_session():
  
  sessions = Session.query.filter_by(user_id = current_user.id)
  try: 
    if request.args.get('page') is None: raise ValueError
    param_page = int(request.args.get('page'))
  except ValueError:
    param_page = 1

  try: 
    param_date = request.args.get('date')
    start = datetime.strptime(param_date, "%Y-%m-%d")
    end = start.replace(hour=23, minute=59)
    sessions = sessions.filter(Session.start >= start).filter(Session.start <= end)
  except:
    pass
  
  sessions = sessions.paginate(page=param_page, per_page= 10).items
  return jsonify(sessions = list(map(lambda session: session.serialize(['user','patient']), sessions)))

def session_params():
  return request.params.require('session').permit("id","start", "end", "patient_id")

def invalid_session():
  return jsonify({"status": "Sessão inválida"}), 404