from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import dotenv
import os

dotenv.load_dotenv()


app = Flask(__name__)
CORS(app)

# Database configuration
DB_CONFIG = {
    'dbname': 'fitness_db',
    'user': 'postgres',
    'password' : os.getenv('DB_POSTGRESQL_PASSWORD'),
    'host': 'localhost',
    'port': '5432'
}

# Database initialization
def init_db():
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS activities (
            id SERIAL PRIMARY KEY,
            calories INTEGER NOT NULL,
            duration INTEGER NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

@app.route('/activities', methods=['GET'])
def get_activities():
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('SELECT id, calories, duration, date FROM activities')
    rows = cursor.fetchall()
    conn.close()
    
    activities = []
    for row in rows:
        activities.append({
            "id": row[0],
            "calories": row[1],
            "duration": row[2],
            "date": row[3]
        })
    return jsonify(activities), 200

@app.route('/activity', methods=['GET'])
def get_activity_by_id():
    activity_id = request.args.get('id', type=int)
    
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('SELECT id, calories, duration, date FROM activities WHERE id = %s', (activity_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        activity = {
            "id": row[0],
            "calories": row[1],
            "duration": row[2],
            "date": row[3]
        }
        return jsonify(activity), 200
    return jsonify({"error": "Activity not found"}), 404

@app.route('/activity', methods=['POST'])
def add_activity():
    new_activity = request.get_json()
    
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO activities (calories, duration, date) VALUES (%s, %s, %s) RETURNING id',
        (new_activity['calories'], new_activity['duration'], new_activity['date'])
    )
    activity_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    
    new_activity['id'] = activity_id
    return jsonify(new_activity), 201

@app.route('/activity', methods=['DELETE'])
def delete_activity():
    activity_id = request.args.get('id', type=int)
    
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM activities WHERE id = %s', (activity_id,))
    row = cursor.fetchone()
    
    if row:
        cursor.execute('DELETE FROM activities WHERE id = %s', (activity_id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Activity deleted"}), 200
    
    conn.close()
    return jsonify({"error": "Activity not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
