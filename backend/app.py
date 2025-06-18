#Backend code
import os
import mysql.connector
from flask import Flask, jsonify, request

app = Flask(__name__)

# Database config
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

@app.route('/')
def index():
    return jsonify({"message": "Backend is running and connected to RDS"})

@app.route('/users', methods=['GET', 'POST'])
def users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        data = request.json
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (data['name'], data['email']))
        conn.commit()
        conn.close()
        return jsonify({"message": "User added"}), 201
    else:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
