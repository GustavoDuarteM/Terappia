from application.models import user
from flask import request, jsonify
from application import app
from application.models.patient import Patient
from application.models.session import Session
from flask_jwt_extended import jwt_required, current_user

@app.route('/patients', methods=['POST'])
@jwt_required()
def new_patients():
  patient = Patient(**patient_params(), user_id = current_user.id )
  if patient.save():
      return jsonify(patient = patient.serialize(['user_id','user','sessions']))
  else:
    return invalid_patient()

@app.route('/patients/<int:id>', methods=['GET'])
@jwt_required()
def show_patients(id):
  patient = Patient.query.filter_by(id = id, user_id = current_user.id).first()
  if patient:
      return jsonify(patient = patient.serialize(['user_id','user','sessions']))
  else:
    return invalid_patient()

@app.route('/patients', methods=['PUT'])
@jwt_required()
def edit_patients():
  params = patient_params()
  patient = Patient.query.filter_by(id= params['id'], user_id= current_user.id).first()
  if not patient : return invalid_patient()
  patient.setattrs(**patient_params())
  if patient.save():
    return jsonify(patient = patient.serialize(['user_id','user','sessions']))
  else:
    return invalid_patient()

@app.route('/patients', methods=['GET'])
@jwt_required()
def all_patients():
  param_page = request.args.get('page')
  param_name = request.args.get('name')
  patients = Patient.query.filter_by(user_id = current_user.id)

  if param_name: 
    search = "%{}%".format(param_name)
    patients = patients.filter(Patient.name.like(search))

  if param_page:
    try: 
      param_page = int(param_page)
    except ValueError:
      param_page = 1

  patients = patients.paginate(page=param_page, per_page= 10).items
  return jsonify(patients = list(map(lambda patient: patient.serialize(['user_id','user','sessions']), patients)))

@app.route('/patients/<int:patient_id>/sessions', methods=['GET'])
@jwt_required()
def patient_sessions(patient_id):
  param_page = request.args.get('page')
  session = Session.query.filter_by(patient_id = patient_id, user_id = current_user.id)
  if param_page:
    try: 
      param_page = int(param_page)
    except ValueError:
      param_page = 1
  sessions = session.paginate(page=param_page, per_page= 10).items
  return jsonify(patient = list(map(lambda session: session.serialize(['user_id','user','patient']), sessions)))

def patient_params():
  return request.params.require('patient').permit("id","name", "email", "phone")

def invalid_patient():
  return jsonify({"status": "Paciente inválido"}), 404