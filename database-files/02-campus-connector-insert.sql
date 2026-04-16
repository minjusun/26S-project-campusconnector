USE campus_connector;

-- a handful of roles so login-ish flows can reference one
INSERT INTO user_roles (role_name) VALUES
    ('student'),
    ('event_coordinator'),
    ('admin');

-- sample users — password_hash is a placeholder, not a real hash
INSERT INTO users (role_id, first_name, last_name, email, password_hash) VALUES
    (1, 'Alex',   'Chen',    'alex.chen@northeastern.edu',    'x'),
    (1, 'Jordan', 'Smith',   'jordan.smith@northeastern.edu', 'x'),
    (2, 'Taylor', 'Nguyen',  'taylor.n@northeastern.edu',     'x'),
    (3, 'Morgan', 'Patel',   'morgan.p@northeastern.edu',     'x'),
    (3, 'Augustus', 'Code', 'augustus.code@northeastern.edu', 'x'),
    (1, 'Horton', 'Brumwell', 'horton.brumwell@northeastern.edu', 'x'),
    (3, 'Brandyn', 'Bonhome', 'brandyn.bonhome@northeastern.edu', 'x'),
    (3, 'Mercy', 'Dowry', 'mercy.dowry@northeastern.edu', 'x'),
    

-- categories students can filter by
INSERT INTO event_categories (category_name) VALUES
    ('Academic'),
    ('Career'),
    ('Social'),
    ('Sports'),
    ('Arts');

-- rooms / venues on campus
INSERT INTO event_location (location_name, capacity) VALUES
    ('Curry Student Center Ballroom', 400),
    ('Snell Library Room 001',        60),
    ('ISEC Auditorium',               250),
    ('Cabot Quad',                    1000);

-- a couple of events to browse (future dates so the "upcoming" filter shows them)
INSERT INTO events (location_id, title, date, start_time, end_time, status, image_url, description) VALUES
    (1, 'Spring Career Fair 2026',      '2026-05-10', '10:00:00', '15:00:00', 'upcoming', NULL, 'Meet recruiters from 80+ companies.'),
    (2, 'CS3200 Study Jam',             '2026-04-28', '18:00:00', '20:00:00', 'upcoming', NULL, 'Group study session before finals.'),
    (3, 'Student Film Screening',       '2026-05-02', '19:00:00', '21:30:00', 'upcoming', NULL, 'Short films produced by students this semester.'),
    (4, 'Intramural Soccer Tournament', '2026-05-15', '09:00:00', '17:00:00', 'upcoming', NULL, 'Bracket-style tournament, open to all majors.');

-- link each event to a category through the join table
INSERT INTO event_category_map (event_id, category_id) VALUES
    (1, 2),  -- Career Fair  -> Career
    (2, 1),  -- Study Jam    -> Academic
    (3, 5),  -- Film         -> Arts
    (4, 4);  -- Soccer       -> Sports

-- a couple of registrations so "My Events" isn't empty for user 1
INSERT INTO registration (event_id, user_id, status) VALUES
    (1, 1, 'registered'),
    (2, 1, 'registered'),
    (3, 2, 'registered');

-- one notification for the student to see
INSERT INTO notifications (user_id, event_id, message) VALUES
    (1, 1, 'Reminder: Spring Career Fair is coming up on May 10!'),
    (1, 2, 'Don''t forget to bring your laptop to the CS3200 study jam.');

INSERT INTO attendance (user_id, event_id, attendance_status) VALUES
    (1, 1, 'checked_in'),
    (2, 3, 'checked_in'),
    (1, 2, 'checked_in');

INSERT INTO waitlist (event_id, user_id, queued_pos, status) VALUES
    (4, 2, 1, 'waiting'),
    (1, 2, 2, 'promoted');

INSERT INTO event_views (event_id, user_id) VALUES
    (1, 1),
    (1, 2),
    (2, 1),
    (3, 2),
    (4, 1);

INSERT INTO comments (user_id, event_id, comment_text, status) VALUES
    (1, 1, 'Looking forward to this event!', 'visible'),
    (2, 2, 'Will there be practice problems at the study jam?', 'visible'),
    (1, 3, 'This sounds really interesting.', 'visible');

INSERT INTO event_history (user_id, event_id, feedback_rating) VALUES
    (1, 1, 5),
    (2, 3, 4),
    (1, 2, 5);

INSERT INTO logs (user_id, action_type, description) VALUES
    (3, 'create_event', 'Created Spring Career Fair 2026'),
    (3, 'create_event', 'Created CS3200 Study Jam'),
    (4, 'view_dashboard', 'Viewed admin dashboard');

INSERT INTO backups (user_id, status) VALUES
    (4, 'completed'),
    (4, 'completed'),
    (4, 'failed');
