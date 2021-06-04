from flask import request, jsonify
from app import app , datetime
from app.models.session import Session

@app.route('/sessions', methods=['POST'])
def new_sessions():
  params = session_params()
  session = Session(**session_params())
  if session.save():
      return jsonify(session.serialize(['user','patient']))
  else:
    return jsonify({"status": "Paciênte inválido"}), 404

@app.route('/sessions/<int:id>', methods=['GET'])
def show_sessions(id):
  session = Session.query.get(id)
  if session:
      return jsonify(session.serialize(['user','patient']))
  else:
    return jsonify({"status": "Sessão inválida"}), 404

@app.route('/sessions', methods=['PUT'])
def edit_sessions():
  params = session_params()
  session = Session.query.get(params['id'])
  session.start =  datetime.strptime(params['start'], "%Y-%m-%d %H:%M")
  session.end = datetime.strptime(params['end'], "%Y-%m-%d %H:%M") 
  if session.save():
      return jsonify(session.serialize(['user','patient']))
  else:
    return jsonify({"status": "Sessão inválida"}), 404

def session_params():
  return request.params.require('session').permit("id","start", "end", "patient_id", "user_id")
