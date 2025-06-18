import boto3
import json
import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_config():
    secret_name = "myapp_secret"
    region_name = "ap-south-1"
    
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    response = client.get_secret_value(SecretId=secret_name)
    secret = json.loads(response['SecretString'])
    return secret

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    creds = get_db_config()
    try:
        conn = mysql.connector.connect(
            host=creds['host'],
            user=creds['username'],
            password=creds['password'],
            database=creds['database'],
            port=int(creds['port'])
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (data['name'], data['email']))
        conn.commit()
        return jsonify({"message": "User added"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
