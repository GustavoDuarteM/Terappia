from flask import request, jsonify
from application import app, datetime
from application.models.session import Session
from application.models.patient import Patient
from flask_jwt_extended import jwt_required, current_user
from application.models.enums.session_status import StatusSessionEnum

@app.route('/sessions', methods=['POST'])
@jwt_required()
def new_sessions():
  params = new_session_params()
  patient = Patient.query.filter_by(id = params['patient_id'], user_id = current_user.id).first()
  if not patient : return invalid_session()
  
  session = Session(**new_session_params(), user_id = current_user.id )
  if not session.valid(): return invalid_session()
  
  if session.save():
      return jsonify(session =  serilize_response(session))
  else:
    return invalid_session()

@app.route('/sessions/<int:id>', methods=['GET'])
@jwt_required()
def show_sessions(id):
  session = Session.query.filter_by(id = id, user_id = current_user.id).first()
  if session:
      return jsonify(session =  serilize_response(session))
  else:
    return invalid_session()

@app.route('/sessions', methods=['PUT'])
@jwt_required()
def edit_sessions():
  params = update_session_params()
  session = Session.query.filter_by(id = params['id'], user_id = current_user.id).first()
  patient = Patient.query.filter_by(id = params['patient_id'], user_id = current_user.id).first()
  if (not session) or (not patient): return invalid_session()

  if params['start'] and params['end']:
    session.start = datetime.strptime(params['start'], "%Y-%m-%d %H:%M")
    session.end = datetime.strptime(params['end'], "%Y-%m-%d %H:%M") 
  if not session.valid(): return invalid_session()

  if params['status']:
    try: 
      status = int(params['status'])
      session.status = StatusSessionEnum(status)
    except ValueError:
      pass

  session.comments = params['comments']
  session.patient = patient

  if session.save():
    return jsonify(session = serilize_response(session))
  else:
    return invalid_session()

@app.route('/sessions', methods=['GET'])
@jwt_required()
def all_session():
  has_next = has_prev = False
  sessions = Session.query.filter_by(user_id = current_user.id)\
                          .order_by(Session.start.desc())
  
  try: 
    param_name = request.args.get('name')
    if param_name:
      search = "%{}%".format(param_name)
      sessions = sessions.join(Patient, Session.patient_id == Patient.id)\
                         .filter(Patient.name.like(search))
  except:
    pass

  try: 
    param_date = request.args.get('date')
    start = datetime.strptime(param_date, "%Y-%m-%d").replace(hour=00, minute=00)
    end = start.replace(hour=23, minute=59)
    sessions = sessions.filter(Session.start >= start)\
                       .filter(Session.start <= end)
  except:
    pass

  try: 
    if request.args.get('page') is None: raise ValueError
    param_page = int(request.args.get('page'))
    sessions = sessions.paginate(page=param_page, per_page= 10)
    has_next = sessions.has_next
    has_prev = sessions.has_prev
    sessions = sessions.items
  except ValueError:
    pass

  return jsonify(sessions = list(map(lambda session: serilize_response(session), sessions)), has_next = has_next, has_prev = has_prev )

@app.route('/sessions/<int:id>', methods=['DELETE'])
@jwt_required()
def session_delete(id):
  session = Session.query.filter_by(id = id, user_id = current_user.id).first()
  if not session : return invalid_session()
  if session.delete():
      return jsonify({"status": "Sessão removida"})
  else:
    return invalid_session()

def new_session_params():
  return request.params.require('session').permit("id","start", "end", "patient_id")

def update_session_params():
  return request.params.require('session').permit("id","start","end","patient_id","status","comments")

def invalid_session():
  return jsonify({"status": "Sessão inválida"}), 404

def serilize_response(session):
  return {**session.serialize(['user_id']),'patient': { **session.patient.serialize(['user_id','sessions'])}}