from flask import Flask, request, jsonify
from app import app

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400

@app.errorhandler(401)
def bad_request(e):
    return jsonify(error=str(e)), 401

@app.errorhandler(500)
def server_error(e):
    return jsonify(error=str(e)), 500