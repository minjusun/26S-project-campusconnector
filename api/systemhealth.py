from flask import Blueprint, jsonify
from backend.db_connection import get_db

systemHealth = Blueprint('systemHealth', __name__)

# user count for system load
@systemHealth.route('/users', methods=['GET'])
def users():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT user_id FROM users")
    return jsonify(cursor.fetchall()), 200


# event data for activity + load
@systemHealth.route('/events', methods=['GET'])
def events():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT event_id, date, status FROM events")
    return jsonify(cursor.fetchall()), 200


# logs for system activity feed
@systemHealth.route('/logs', methods=['GET'])
def logs():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT log_id, user_id, action_type, description, created_at
        FROM logs
        ORDER BY created_at DESC
    """)
    return jsonify(cursor.fetchall()), 200


# backups for system health signal
@systemHealth.route('/backups', methods=['GET'])
def backups():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT backup_id, status FROM backups")
    return jsonify(cursor.fetchall()), 200