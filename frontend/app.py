from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        response = requests.get("http://backend-service:5000/api", timeout=3)
        return f"Frontend → Backend: {response.json()['message']}"
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
