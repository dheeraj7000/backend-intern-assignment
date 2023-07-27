# error_handlers.py
from flask import jsonify

def not_found(error):
    return jsonify({"error": "Not found"}), 404

def bad_request(error):
    return jsonify({"error": "Bad request"}), 400
