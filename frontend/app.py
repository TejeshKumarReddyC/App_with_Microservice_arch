import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5000")

@app.route('/')
def index():
    try:
        print(f"Connecting to: {BACKEND_URL}")
        response = requests.get(f"{BACKEND_URL}/users")
        return jsonify(response.json())
    except Exception as e:
        return f"Error connecting to backend: {e}", 500
