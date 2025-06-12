from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)
BACKEND_URL = "http://backend:5000/messages"

TEMPLATE = '''
<form method="POST">
    <input name="msg"><input type="submit">
</form>
<ul>{% for msg in messages %}<li>{{ msg }}</li>{% endfor %}</ul>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        requests.post(BACKEND_URL, json={"content": request.form["msg"]})
    res = requests.get(BACKEND_URL)
    return render_template_string(TEMPLATE, messages=res.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0')

