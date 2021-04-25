from flask import Flask, request, jsonify
from app import app

@app.route('/sign_out', methods=['POST'])
def sign_out():
    user = request.params.require('user').permit('id')
    return jsonify(user)