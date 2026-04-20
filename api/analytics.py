from flask import Blueprint, jsonify
from backend.db_connection import get_db
from datetime import datetime

analytics = Blueprint('analytics', __name__)


@analytics.route('/analytics/event-performance-detailed', methods=['GET'])
def event_performance_detailed():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute('''
        SELECT e.event_id, e.title,
               el.capacity,
               (SELECT COUNT(*) FROM registration r
                WHERE r.event_id = e.event_id) AS registrations,
               (SELECT COUNT(*) FROM registration r
                WHERE r.event_id = e.event_id
                  AND r.status = 'registered') AS attendance,
               (SELECT COUNT(*) FROM comments c
                WHERE c.event_id = e.event_id) AS comments
        FROM events e
        JOIN event_location el ON e.location_id = el.location_id
        GROUP BY e.event_id, e.title, el.capacity
    ''')

    events = cursor.fetchall()

    best_event = None
    total_rate = 0.0

    for e in events:
        capacity = int(e["capacity"] or 1)
        attendance = int(e["attendance"] or 0)
        e["registrations"] = int(e["registrations"] or 0)
        e["attendance"] = attendance
        e["comments"] = int(e["comments"] or 0)

        e["attendance_rate"] = attendance / capacity if capacity else 0.0
        total_rate += e["attendance_rate"]

        if not best_event or e["attendance_rate"] > best_event["attendance_rate"]:
            best_event = e

    avg_attendance_rate = total_rate / len(events) if events else 0

    cursor.close()
    db.close()

    return jsonify({
        "best_event": best_event,
        "avg_attendance_rate": avg_attendance_rate,
        "events": events
    }), 200


@analytics.route('/analytics/insights', methods=['GET'])
def insights():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute('''
        SELECT e.event_id, e.date,
               (SELECT ec.category_name
                FROM event_category_map ecm
                JOIN event_categories ec
                  ON ecm.category_id = ec.category_id
                WHERE ecm.event_id = e.event_id
                LIMIT 1) AS category,
               COUNT(r.registration_id) AS attendance
        FROM events e
        LEFT JOIN registration r
          ON e.event_id = r.event_id
         AND r.status = 'registered'
        GROUP BY e.event_id
    ''')

    events = cursor.fetchall()

    category_totals = {}
    category_avg = []
    best_category = None

    for e in events:
        cat = e["category"] or "Other"

        if cat not in category_totals:
            category_totals[cat] = {"sum": 0, "count": 0}

        category_totals[cat]["sum"] += int(e["attendance"] or 0)
        category_totals[cat]["count"] += 1

    for cat in category_totals:
        avg = category_totals[cat]["sum"] / category_totals[cat]["count"]

        item = {
            "category": cat,
            "predicted_attendance": int(avg)
        }

        category_avg.append(item)

        if not best_category or avg > best_category["predicted_attendance"]:
            best_category = item

    day_totals = {}
    best_day = None

    for e in events:
        date_val = e["date"]
        if date_val is None:
            continue
        if isinstance(date_val, str):
            dt = datetime.fromisoformat(date_val)
        else:
            dt = datetime.combine(date_val, datetime.min.time())
        day = dt.strftime("%A")

        if day not in day_totals:
            day_totals[day] = {"sum": 0, "count": 0}

        day_totals[day]["sum"] += int(e["attendance"] or 0)
        day_totals[day]["count"] += 1

    for d in day_totals:
        avg = day_totals[d]["sum"] / day_totals[d]["count"]

        if not best_day or avg > best_day["avg"]:
            best_day = {
                "day": d,
                "avg": avg
            }

    cursor.close()
    db.close()

    return jsonify({
        "best_category": best_category,
        "best_day": best_day,
        "predictions": category_avg
    }), 200
