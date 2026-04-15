from flask import Blueprint, request, jsonify
from backend.db_connection import get_db

engagement = Blueprint('engagement', __name__)


@engagement.route('/registration', methods=['GET'])
def get_registrations():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM registration ORDER BY registered_at DESC')
    return jsonify(cursor.fetchall()), 200


@engagement.route('/registration', methods=['POST'])
def create_registration():
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''INSERT INTO registration (event_id, user_id, status)
                      VALUES (%s, %s, %s)''',
                   (data['event_id'], data['user_id'],
                    data.get('status', 'registered')))
    new_id = cursor.lastrowid
    db.commit()
    return jsonify({'message': 'Registered successfully',
                    'registration_id': new_id}), 201


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
    cursor = db.cursor(dictionary=True)
    # category comes from the event_category_map join table
    cursor.execute('''SELECT r.registration_id, e.event_id, e.title,
                             CAST(e.date AS CHAR) AS date,
                             CAST(e.start_time AS CHAR) AS start_time,
                             CAST(e.end_time AS CHAR) AS end_time,
                             e.status AS event_status, r.status,
                             r.registered_at,
                             (SELECT ec.category_name
                              FROM event_category_map ecm
                              JOIN event_categories ec
                                ON ecm.category_id = ec.category_id
                              WHERE ecm.event_id = e.event_id
                              LIMIT 1) AS category_name
                      FROM registration r
                      JOIN events e ON r.event_id = e.event_id
                      WHERE r.user_id = %s
                      ORDER BY e.date, e.start_time''', (id,))
    return jsonify(cursor.fetchall()), 200


@engagement.route('/events/<int:id>/registration', methods=['GET'])
def get_event_registrations(id):
    # roster for a single event (used by the coordinator attendance page)
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('''SELECT r.registration_id, r.user_id, r.status,
                             r.registered_at, u.first_name, u.last_name,
                             u.email
                      FROM registration r
                      JOIN users u ON r.user_id = u.user_id
                      WHERE r.event_id = %s
                      ORDER BY r.registered_at''', (id,))
    return jsonify(cursor.fetchall()), 200
