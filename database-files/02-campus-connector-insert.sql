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
    (1, 'Batholomew', 'De Freyne', 'batholomew.de freyne@northeastern.edu', 'x'),
    (1, 'Lindsey', 'Tysack', 'lindsey.tysack@northeastern.edu', 'x'), 
    (2, 'Darya', 'Brocket', 'darya.brocket@northeastern.edu', 'x'),
    (1, 'Tally', 'Weiner', 'tally.weiner@northeastern.edu', 'x'),
    (2, 'Matthew', 'Renfield', 'matthew.renfield@northeastern.edu', 'x'),
    (3, 'Aryn', 'Bydaway', 'aryn.bydaway@northeastern.edu', 'x'),
    (1, 'Farly', 'De la Perrelle', 'farly.de la perrelle@northeastern.edu', 'x'),
    (2, 'Maribelle', 'Codi', 'maribelle.codi@northeastern.edu', 'x'),
    (3, 'Irma', 'Root', 'irma.root@northeastern.edu', 'x'),
    (1, 'Sutherlan', 'MacKim', 'sutherlan.mackim@northeastern.edu', 'x'),
    (3, 'Damaris', 'Payfoot', 'damaris.payfoot@northeastern.edu', 'x'),
    (3, 'Holly-anne', 'Muscroft', 'holly-anne.muscroft@northeastern.edu', 'x'),
    (1, 'Griz', 'Nendick', 'griz.nendick@northeastern.edu', 'x'),
    (3, 'Zaria', 'Garralts', 'zaria.garralts@northeastern.edu', 'x'),
    (3, 'Carr', 'Dockerty', 'carr.dockerty@northeastern.edu', 'x'),
    (1, 'Hugh', 'Heibl', 'hugh.heibl@northeastern.edu', 'x');

-- categories students can filter by
INSERT INTO event_categories (category_name) VALUES
    ('Academic'),
    ('Career'),
    ('Social'),
    ('Sports'),
    ('Arts');

-- rooms/venues on campus
INSERT INTO event_location (location_name, capacity) VALUES
    ('Curry Student Center Ballroom', 400),
    ('Snell Library Room 001',         60),
    ('ISEC Auditorium',               250),
    ('Cabot Quad',                    1000)
    ('Richards Hall Room 120',          80),
    ('West Village H Room 108',         70),
    ('Behrakis Health Sciences Center Room 215', 120),
    ('Shillman Hall Room 305',         100),
    ('Forsyth Building Room 201',       90),
    ('Ell Hall Auditorium',             200),
    ('Marino Recreation Center Gymnasium', 500),
    ('ISEC Room 102', 7                   5),
    ('EXP Building Event Space',         300),
    ('Curry Student Center Room 333',     60),
    ('Hayden Hall Room 101',             110),
    ('Dodge Hall Room 250',                85),
    ('Robinson Hall Room 109',             95),
    ('Snell Library Quad Study Area',     150),
    ('Centennial Common Outdoor Stage',   600);

-- a couple of events to browse (future dates so the "upcoming" filter shows them)
INSERT INTO events (location_id, title, date, start_time, end_time, status, image_url, description) VALUES
(1, 'Spring Career Fair 2026', '2026-05-10', '10:00:00', '15:00:00', 'upcoming', NULL, 'Meet recruiters from 80+ companies.'),
(2, 'CS3200 Study Jam', '2026-04-28', '18:00:00', '20:00:00', 'upcoming', NULL, 'Group study session before finals.'),
(3, 'Student Film Screening', '2026-05-02', '19:00:00', '21:30:00', 'upcoming', NULL, 'Short films produced by students this semester.'),
(4, 'Intramural Soccer Tournament', '2026-05-15', '09:00:00', '17:00:00', 'upcoming', NULL, 'Bracket-style tournament, open to all majors.'),
(14, 'Data Science Networking Night', '2026-05-22', '11:26', '17:04', 'upcoming', NULL, 'Connect with fellow students and professionals interested in data science and analytics.'),
(6, 'AI & Machine Learning Panel', '2026-06-26', '13:59', '15:06', 'upcoming', NULL, 'Join industry experts as they discuss the latest trends in artificial intelligence and machine learning.'),
(8, 'Resume & LinkedIn Workshop', '2026-04-29', '09:33', '13:10', 'upcoming', NULL, 'Improve your resume and LinkedIn profile with guidance from career advisors.'),
(16, 'Startup Founder Speaker Series', '2026-06-08', '12:35', '20:04', 'upcoming', NULL, 'Hear from startup founders about their journey and lessons learned in building a company.'),
(7, 'Finance Career Insights Session', '2026-06-24', '16:53', '21:12', 'upcoming', NULL, 'Learn about career paths and opportunities in finance from industry professionals.'),
(13, 'Tech Internship Info Session', '2026-05-16', '10:44', '17:15', 'upcoming', NULL, 'Get insights into securing internships in the tech industry and how to stand out.'),
(19, 'Women in STEM Networking Event', '2026-06-11', '15:23', '17:13', 'upcoming', NULL, 'Network with inspiring women in STEM fields and build meaningful connections.'),
(14, 'Cybersecurity Awareness Workshop', '2026-05-16', '09:10', '20:14', 'upcoming', NULL, 'Learn the fundamentals of cybersecurity and how to protect digital information.'),
(17, 'Product Management Crash Course', '2026-05-16', '16:36', '19:52', 'upcoming', NULL, 'A crash course on product management covering key skills and real-world applications.'),
(19, 'Consulting Case Prep Workshop', '2026-05-17', '09:49', '18:11', 'upcoming', NULL, 'Practice solving consulting case interviews and improve your problem-solving skills.'),
(12, 'Entrepreneurship Pitch Night', '2026-06-02', '15:43', '17:46', 'upcoming', NULL, 'Pitch your business ideas and receive feedback from peers and mentors.'),
(17, 'K-Pop Dance Showcase', '2026-06-15', '14:42', '17:39', 'upcoming', NULL, 'Enjoy performances of popular K-pop dances by student groups.'),
(17, 'Open Mic Night at Curry', '2026-05-22', '13:33', '15:56', 'upcoming', NULL, 'Showcase your talent or enjoy performances in a relaxed open mic setting.'),
(12, 'Spring Club Fair', '2026-05-27', '09:07', '15:40', 'upcoming', NULL, 'Discover different student organizations and get involved on campus.'),
(6, 'Mental Health & Wellness Seminar', '2026-06-16', '16:13', '19:24', 'upcoming', NULL, 'Learn strategies for maintaining mental health and overall wellness during college.');

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
