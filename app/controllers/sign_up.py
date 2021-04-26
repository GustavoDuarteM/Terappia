from flask import Flask, request, jsonify
from app import app
from app.models.user import User

@app.route('/sign_up', methods=['POST'])
def sign_up():
    user = User(**sign_up_user_params())
    if user.save():
      return jsonify(user.serialize())
    else:
      return jsonify({"status": "usuário inválido"}), 404

def sign_up_user_params():
    return request.params.require('user').permit("name", "email", "password", "phone")

