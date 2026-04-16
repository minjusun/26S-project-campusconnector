from flask import Blueprint, request, jsonify
from backend.db_connection import get_db

users = Blueprint('users', __name__)

# endpoints for user management (admin can manage users, and users can view/update their own profile)
@users.route('/users', methods=['GET'])
def get_users():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('''SELECT user_id, role_id, first_name, last_name, email,
                             status, created_at
                      FROM users
                      ORDER BY user_id''')
    rows = cursor.fetchall()
    return jsonify(rows), 200

# get a single user by ID
@users.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('''SELECT user_id, role_id, first_name, last_name, email,
                             status, created_at
                      FROM users
                      WHERE user_id = %s''', (id,))
    row = cursor.fetchone()
    return jsonify(row), 200

# create a new user (admin only)
@users.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''INSERT INTO users (role_id, first_name, last_name, email, status, password_hash)
                      VALUES (%s, %s, %s, %s, %s, %s)''',
                   (data['role_id'], data['first_name'], data['last_name'],
                    data['email'], data.get('status', 'active'), data['password_hash']))
    db.commit()
    return jsonify({'message': 'User created'}), 201

# update user information (admin can update any user, users can update their own profile)
@users.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''UPDATE users SET email = %s, role_id = %s, status = %s
                      WHERE user_id = %s''',
                   (data['email'], data['role_id'], data['status'], id))
    db.commit()
    return jsonify({'message': 'User updated'}), 200

# delete a user (admin only)
@users.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM users WHERE user_id = %s', (id,))
    db.commit()
    return jsonify({'message': 'User deleted'}), 200
