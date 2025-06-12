from flask import Flask, request, jsonify
import pymysql
import os

app = Flask(__name__)

db_host = os.environ['DB_HOST']
db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PASS']
db_name = os.environ['DB_NAME']

conn = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name)

@app.route('/message',methods=['POST'])
def add_message():
    data = request.get_json()
    with conn.cursor() as cur:
        cur.execute("INSERT INTO messages (content) VALUES (%s)", (data['content'],))
        conn.commit()
    return jsonify({"status": "added"}), 201
@app.route('/messages', methods=['GET'])
def get_messages():
    with conn.cursor() as cur:
        cur.execute("SELECT content FROM messages")
        results = cur.fetchall()
    return jsonify([row[0] for row in results])
if __name__ == '__main__':
    app.run(host='0.0.0.0')

