from flask import Blueprint, request, jsonify
from backend.db_connection import get_db

engagement = Blueprint('engagement', __name__)

@engagement.route('/registration', methods=['GET'])
def get_registrations():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM registration')
    rows = cursor.fetchall()
    return jsonify(rows), 200

@engagement.route('/registration', methods=['POST'])
def create_registration():
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''INSERT INTO registration (event_id, user_id, status)
                      VALUES (%s, %s, %s)''',
                   (data['event_id'], data['user_id'], data['status']))
    db.commit()
    return jsonify({'message': 'Registered successfully'}), 201

@engagement.route('/registration/<int:id>', methods=['PUT'])
def update_registration(id):
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''UPDATE registration SET status = %s 
                      WHERE registration_id = %s''',
                   (data['status'], id))
    db.commit()
    return jsonify({'message': 'Registration updated'}), 200

@engagement.route('/registration/<int:id>', methods=['DELETE'])
def delete_registration(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM registration WHERE registration_id = %s', (id,))
    db.commit()
    return jsonify({'message': 'Registration cancelled'}), 200

@engagement.route('/users/<int:id>/registration', methods=['GET'])
def get_user_registrations(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''SELECT e.event_id, e.title, e.date, 
                      e.start_time, e.end_time, r.status
                      FROM registration r
                      JOIN events e ON r.event_id = e.event_id
                      WHERE r.user_id = %s
                      ORDER BY e.date''', (id,))
    rows = cursor.fetchall()
    return jsonify(rows), 200