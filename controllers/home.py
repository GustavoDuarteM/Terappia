from application import app
from flask import jsonify

@app.route('/sign_in', methods=["POST"])
def sign_in():
  response = {"status":"logado"}
  return jsonify(response)