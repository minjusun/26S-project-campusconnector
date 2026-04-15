from flask import Blueprint, request, jsonify
from backend.db_connection import get_db

events = Blueprint('events', __name__)

# events and categories are linked through the event_category_map join
# table, so we pull the category name with a small subquery instead of a
# regular JOIN (keeps one row per event even if an event ends up tagged
# with more than one category later on).
CATEGORY_SUBQUERY = '''(SELECT ec.category_name
                        FROM event_category_map ecm
                        JOIN event_categories ec
                          ON ecm.category_id = ec.category_id
                        WHERE ecm.event_id = e.event_id
                        LIMIT 1) AS category_name'''

CATEGORY_ID_SUBQUERY = '''(SELECT ecm.category_id
                           FROM event_category_map ecm
                           WHERE ecm.event_id = e.event_id
                           LIMIT 1) AS category_id'''


@events.route('/events', methods=['GET'])
def get_events():
    # optional query params: category, status, upcoming, q
    db = get_db()
    cursor = db.cursor(dictionary=True)

    category = request.args.get('category')
    status = request.args.get('status')
    upcoming = request.args.get('upcoming')
    q = request.args.get('q')

    query = f'''SELECT e.event_id, e.title,
                       CAST(e.date AS CHAR) AS date,
                       CAST(e.start_time AS CHAR) AS start_time,
                       CAST(e.end_time AS CHAR) AS end_time,
                       e.status, e.location_id,
                       el.location_name, el.capacity,
                       {CATEGORY_SUBQUERY},
                       {CATEGORY_ID_SUBQUERY}
                FROM events e
                JOIN event_location el ON e.location_id = el.location_id
                WHERE 1=1'''
    params = []

    if category:
        query += ''' AND EXISTS (
                        SELECT 1 FROM event_category_map ecm
                        JOIN event_categories ec
                          ON ecm.category_id = ec.category_id
                        WHERE ecm.event_id = e.event_id
                          AND ec.category_name = %s)'''
        params.append(category)
    if status:
        query += ' AND e.status = %s'
        params.append(status)
    if upcoming and upcoming.lower() in ('true', '1', 'yes'):
        query += ' AND e.date >= CURDATE()'
    if q:
        query += ' AND e.title LIKE %s'
        params.append(f'%{q}%')

    query += ' ORDER BY e.date, e.start_time'
    cursor.execute(query, params)
    return jsonify(cursor.fetchall()), 200


@events.route('/events/<int:id>', methods=['GET'])
def get_event(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute(f'''SELECT e.event_id, e.title, e.description,
                              CAST(e.date AS CHAR) AS date,
                              CAST(e.start_time AS CHAR) AS start_time,
                              CAST(e.end_time AS CHAR) AS end_time,
                              e.status, e.image_url, e.location_id,
                              el.location_name, el.capacity,
                              {CATEGORY_SUBQUERY},
                              {CATEGORY_ID_SUBQUERY}
                       FROM events e
                       JOIN event_location el
                         ON e.location_id = el.location_id
                       WHERE e.event_id = %s''', (id,))
    row = cursor.fetchone()
    if not row:
        return jsonify(None), 404
    return jsonify(row), 200


@events.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''INSERT INTO events (location_id, title, date,
                      start_time, end_time, status, image_url, description)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',
                   (data['location_id'], data['title'], data['date'],
                    data['start_time'], data['end_time'], data['status'],
                    data.get('image_url'), data.get('description')))
    new_id = cursor.lastrowid

    # link to a category through the join table
    category_id = data.get('category_id')
    if category_id:
        cursor.execute('''INSERT INTO event_category_map (event_id, category_id)
                          VALUES (%s, %s)''', (new_id, category_id))

    db.commit()
    return jsonify({'message': 'Event created', 'event_id': new_id}), 201


@events.route('/events/<int:id>', methods=['PUT'])
def update_event(id):
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''UPDATE events
                      SET title = %s, date = %s, start_time = %s,
                          end_time = %s, location_id = %s,
                          status = %s, image_url = %s, description = %s
                      WHERE event_id = %s''',
                   (data['title'], data['date'], data['start_time'],
                    data['end_time'], data['location_id'],
                    data['status'], data.get('image_url'),
                    data.get('description'), id))

    # refresh the category link — wipe old rows then insert the new one
    category_id = data.get('category_id')
    if category_id:
        cursor.execute('DELETE FROM event_category_map WHERE event_id = %s', (id,))
        cursor.execute('''INSERT INTO event_category_map (event_id, category_id)
                          VALUES (%s, %s)''', (id, category_id))

    db.commit()
    return jsonify({'message': 'Event updated'}), 200


@events.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    db = get_db()
    cursor = db.cursor()
    # event_category_map has ON DELETE CASCADE so it cleans itself up
    cursor.execute('DELETE FROM events WHERE event_id = %s', (id,))
    db.commit()
    return jsonify({'message': 'Event deleted'}), 200


@events.route('/event_categories', methods=['GET'])
def get_categories():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT category_id, category_name FROM event_categories ORDER BY category_name')
    return jsonify(cursor.fetchall()), 200


@events.route('/event_location', methods=['GET'])
def get_locations():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('''SELECT location_id, location_name, capacity
                      FROM event_location
                      ORDER BY location_name''')
    return jsonify(cursor.fetchall()), 200
