from flask import request, jsonify
from app import app
from app.models.patient import Patient

@app.route('/patients', methods=['POST'])
def new_patients():
  patient = Patient(**patient_params())
  if patient.save():
      return jsonify(patient.serialize(['user']))
  else:
    return jsonify({"status": "Paciênte inválido"}), 404


def patient_params():
  return request.params.require('patient').permit("name", "email", "phone", "user_id")
