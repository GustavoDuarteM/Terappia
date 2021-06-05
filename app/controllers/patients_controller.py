from app.models import user
from flask import request, jsonify
from app import app
from app.models.patient import Patient
from flask_jwt_extended import jwt_required, current_user

@app.route('/patients', methods=['POST'])
@jwt_required()
def new_patients():
  patient = Patient(**patient_params(), user_id = current_user.id )
  if patient.save():
      return jsonify(patient = patient.serialize(['user','sessions']))
  else:
    return jsonify({"status": "Paciênte inválido"}), 404

@app.route('/patients/<int:id>', methods=['GET'])
@jwt_required()
def show_patients(id):
  patient = Patient.query.filter_by(id = id, user_id = current_user.id).first()
  if patient:
      return jsonify(patient = patient.serialize(['user','sessions']))
  else:
    return jsonify({"status": "Paciente inválido"}), 404

@app.route('/patients', methods=['PUT'])
@jwt_required()
def edit_patients():
  params = patient_params()
  patient = Patient.query.filter_by(id= params['id'], user_id= current_user.id).first()
  patient.setattrs(**patient_params())
  if patient.save():
    return jsonify(patient = patient.serialize(['user','sessions']))
  else:
    return jsonify({"status": "Paciênte inválido"}), 404

def patient_params():
  return request.params.require('patient').permit("id","name", "email", "phone")