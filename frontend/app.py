import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Backend base URL from environment
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5000")


@app.route('/')
def index():
    try:
        response = requests.get(f"{BACKEND_URL}/users")
        return jsonify(response.json())
    except Exception as e:
        return f"Error connecting to backend: {e}", 500


@app.route('/add-user', methods=['POST'])
def add_user():
    try:
        data = request.json
        response = requests.post(f"{BACKEND_URL}/users", json=data)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return f"Error adding user: {e}", 500
