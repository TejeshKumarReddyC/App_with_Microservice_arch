from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/api")
def backend_api():
    try:
        conn = psycopg2.connect(
            dbname=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            host=os.environ['DB_HOST'],
            port=os.environ.get('DB_PORT', 5432)
        )
        cur = conn.cursor()
        cur.execute("SELECT 'Hello from RDS!'")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result[0]
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
