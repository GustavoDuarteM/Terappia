from flask import request, jsonify
from app import app
from app.models.patient import Patient
from flask_jwt_extended import jwt_required

@app.route('/patients', methods=['POST'])
@jwt_required()
def new_patients():
  patient = Patient(**patient_params())
  if patient.save():
      return jsonify(patient.serialize(['user']))
  else:
    return jsonify({"status": "Paciênte inválido"}), 404

@app.route('/patients/<int:id>', methods=['GET'])
@jwt_required()
def show_patients(id):
  patient = Patient.query.get(id)
  if patient:
      return jsonify(patient.serialize(['user']))
  else:
    return jsonify({"status": "Paciente inválido"}), 404

@app.route('/patients', methods=['PUT'])
@jwt_required()
def edit_patients():
  params = patient_params()
  patient = Patient.query.get(params['id'])
  patient.setattrs(**patient_params())
  if patient.save():
      return jsonify(patient.serialize(['user']))
  else:
    return jsonify({"status": "Paciênte inválido"}), 404

def patient_params():
  return request.params.require('patient').permit("id","name", "email", "phone", "user_id")
