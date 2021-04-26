from flask import Flask, request, jsonify
from app import app, bcrypt
from app.models.user import User

@app.route('/sign_in', methods=['POST'])
def sign_in_user():    
  user = validate_user(sign_in_user_params())
  if not user is None:
    return jsonify(user.serialize())
  else:
    return jsonify({"status": "usuário inválido"}), 404

def validate_user(_user):  
  try:
    user = User.query.filter_by(email=_user['email']).first()
    if bcrypt.check_password_hash(user.password_hash, _user['password']): 
      return user
    else:
      return None
  except:
    return None

def sign_in_user_params():
  return request.params.require('user').permit('email', 'password')