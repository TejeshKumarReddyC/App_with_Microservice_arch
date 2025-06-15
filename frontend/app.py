from flask import Flask
import requests

app = Flask(__name__)
BACKEND_URL = "http://backend:5000/api"

@app.route("/")
def index():
    try:
        response = requests.get(BACKEND_URL)
        return f"<h1>Frontend</h1><p>Backend says: {response.text}</p>"
    except Exception as e:
        return f"<h1>Frontend</h1><p>Error contacting backend: {e}</p>", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
