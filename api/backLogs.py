from flask import Blueprint, request, jsonify
from backend.db_connection import get_db

backlogs = Blueprint('backlogs', __name__)

#returns notifications for specific user, else returns all-made date format more readable
#returns notification ID, event info, message, date, etc.
@backlogs.route('/notifications', methods=['GET'])
def get_notifications():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    user_id = request.args.get('user_id')
    if user_id:
        cursor.execute('''SELECT notification_id, user_id, event_id, message,
                                 CAST(sent_at AS CHAR) AS sent_at
                          FROM notifications
                          WHERE user_id = %s
                          ORDER BY sent_at DESC''', (user_id,))
    else:
        cursor.execute('''SELECT notification_id, user_id, event_id, message,
                                 CAST(sent_at AS CHAR) AS sent_at
                          FROM notifications
                          ORDER BY sent_at DESC''')
    rows = cursor.fetchall()
    return jsonify(rows), 200

# create a new notification for a user
@backlogs.route('/notifications', methods=['POST'])
def create_notification():
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''INSERT INTO notifications (user_id, event_id, message)
                      VALUES (%s, %s, %s)''',
                   (data['user_id'], data['event_id'], data['message']))
    db.commit()
    return jsonify({'message': 'Notification created'}), 201

# delete a notification by ID
@backlogs.route('/notifications/<int:id>', methods=['DELETE'])
def delete_notification(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM notifications WHERE notification_id = %s', (id,))
    db.commit()
    return jsonify({'message': 'Notification deleted'}), 200

# Logs endpoints for admin monitoring
@backlogs.route('/logs', methods=['GET'])
def get_logs():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('''SELECT log_id, user_id, action_type, description, created_at 
                      FROM logs 
                      ORDER BY created_at DESC''')
    rows = cursor.fetchall()
    return jsonify(rows), 200

# Create a new log entry
@backlogs.route('/logs', methods=['POST'])
def create_log():
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''INSERT INTO logs (user_id, action_type, description)
                      VALUES (%s, %s, %s)''',
                   (data['user_id'], data['action_type'], data['description']))
    db.commit()
    return jsonify({'message': 'Log created'}), 201