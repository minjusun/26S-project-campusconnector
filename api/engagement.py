from flask import Blueprint, request, jsonify
from backend.db_connection import get_db

engagement = Blueprint('engagement', __name__)

# for user engagement features like event registration and comments
@engagement.route('/registration', methods=['GET'])
def get_registrations():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM registration ORDER BY registered_at DESC')
    return jsonify(cursor.fetchall()), 200

# create a new registration for an event
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

# update registration status (e.g. for attendance tracking or cancellation)
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

# delete a registration (e.g. for cancellation)
@engagement.route('/registration/<int:id>', methods=['DELETE'])
def delete_registration(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM registration WHERE registration_id = %s', (id,))
    db.commit()
    return jsonify({'message': 'Registration cancelled'}), 200

# comments endpoints for users to comment on events, with optional status for moderation
@engagement.route('/users/<int:id>/comments', methods=['GET'])
def get_user_comments(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''SELECT c.comment_id, c.event_id, c.comment_text, 
                      c.status, c.created_at
                      FROM comments c
                      WHERE c.user_id = %s
                      ORDER BY c.created_at DESC''', (id,))
    rows = cursor.fetchall()
    return jsonify(rows), 200

# create a new comment for an event
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
