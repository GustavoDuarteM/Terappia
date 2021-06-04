from flask import request, jsonify
from app import app
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

def session_params():
  return request.params.require('session').permit("start", "end", "patient_id", "user_id")
