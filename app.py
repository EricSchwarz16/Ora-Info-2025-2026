from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
import config  # Import database credentials from config.py

app = Flask(__name__)

# Connect to PostgreSQL database
def get_db_connection():
    conn = psycopg2.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        database=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD
    )
    return conn

@app.route('/')
def home():
    return 'Welcome to the Booking Platform API!'

# Endpoint to get all services
@app.route('/services', methods=['GET'])
def get_services():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM Services')
    services = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(services)

# Endpoint to get doctor availability
@app.route('/availability', methods=['GET'])
def get_availability():
    doctor_id = request.args.get('doctor_id')  # Get doctor ID from query params
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM Availability WHERE doctor_id = %s', (doctor_id,))
    availability = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(availability)

# Endpoint to create a new appointment
@app.route('/appointments', methods=['POST'])
def create_appointment():
    user_id = request.json['user_id']
    service_id = request.json['service_id']
    appointment_time = request.json['appointment_time']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO Appointments (user_id, service_id, appointment_time, status) '
        'VALUES (%s, %s, %s, %s) RETURNING *',
        (user_id, service_id, appointment_time, 'pending')
    )
    new_appointment = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify(new_appointment)

# Endpoint to process payment
@app.route('/payments', methods=['POST'])
def create_payment():
    appointment_id = request.json['appointment_id']
    payment_date = request.json['payment_date']
    amount = request.json['amount']
    payment_status = request.json['payment_status']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO Payments (appointment_id, payment_date, amount, payment_status) '
        'VALUES (%s, %s, %s, %s) RETURNING *',
        (appointment_id, payment_date, amount, payment_status)
    )
    new_payment = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify(new_payment)

if __name__ == '__main__':
    app.run(debug=True)
