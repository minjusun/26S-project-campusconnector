from flask import Blueprint, request, jsonify
from backend.db_connection import get_db

events = Blueprint('events', __name__)

@events.route('/events', methods=['GET'])
def get_events():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''SELECT e.event_id, e.title, e.date, 
                      CAST(e.start_time AS CHAR), 
                      CAST(e.end_time AS CHAR),
                      e.status, el.capacity
                      FROM events e
                      JOIN event_location el ON e.location_id = el.location_id
                      ORDER BY e.date, e.start_time''')
    rows = cursor.fetchall()
    return jsonify(rows), 200

@events.route('/events/<int:id>', methods=['GET'])
def get_event(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''SELECT e.event_id, e.title, e.description, e.date, 
                      CAST(e.start_time AS CHAR),
                      CAST(e.end_time AS CHAR),
                      e.status, e.image_url,
                      el.capacity, el.location_id
                      FROM events e
                      JOIN event_location el ON e.location_id = el.location_id
                      WHERE e.event_id = %s''', (id,))
    row = cursor.fetchone()
    return jsonify(row), 200

@events.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''INSERT INTO events (category_id, location_id, title, date,
                      start_time, end_time, status, image_url, description)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                   (data['category_id'], data['location_id'], data['title'],
                    data['date'], data['start_time'], data['end_time'],
                    data['status'], data.get('image_url'), data.get('description')))
    db.commit()
    return jsonify({'message': 'Event created'}), 201

@events.route('/events/<int:id>', methods=['PUT'])
def update_event(id):
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''UPDATE events SET title = %s, date = %s, start_time = %s,
                      end_time = %s, location_id = %s, status = %s, image_url = %s
                      WHERE event_id = %s''',
                   (data['title'], data['date'], data['start_time'],
                    data['end_time'], data['location_id'], data['status'],
                    data.get('image_url'), id))
    db.commit()
    return jsonify({'message': 'Event updated'}), 200

@events.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM events WHERE event_id = %s', (id,))
    db.commit()
    return jsonify({'message': 'Event deleted'}), 200