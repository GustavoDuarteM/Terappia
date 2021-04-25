from flask import Flask, request, jsonify
from app import app

@app.route('/sign_in', methods=['POST'])
def sign_in():
    user = request.params.require('user').permit('name', 'password')
    return jsonify(user)