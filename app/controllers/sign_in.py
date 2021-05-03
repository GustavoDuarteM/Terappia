from flask import request, jsonify
from app import app
from app.models.user import User
from flask_jwt_extended import create_access_token

@app.route('/sign_in', methods=['POST'])
def sign_in_user():    
  user = validate_user(sign_in_user_params())
  if user:
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token)
  else:
    return jsonify({"status": "usuário inválido"}), 401

def validate_user(_user):
  try:
    user = User.query.filter_by(email=_user['email']).first()
    if user and user.check_password(_user['password']):
      return user
  except:
    return None

def sign_in_user_params():
  return request.params.require('user').permit('email', 'password')