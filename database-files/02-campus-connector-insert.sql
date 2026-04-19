USE campus_connector;

-- a handful of roles so login-ish flows can reference one
INSERT INTO user_roles (role_name) VALUES
    ('student'),
    ('event_coordinator'),
    ('admin');

-- sample users — password_hash is a placeholder, not a real hash
INSERT INTO users (role_id, first_name, last_name, email, password_hash) VALUES
    (1, 'John',   'Smith',   'john.smith@northeastern.edu',    'x'),
    (1, 'Jordan', 'Smith',   'jordan.smith@northeastern.edu', 'x'),
    (2, 'Alexa',  'Ziti',    'alexa.ziti@northeastern.edu',   'x'),
    (3, 'Morgan', 'Patel',   'morgan.p@northeastern.edu',     'x'),
    (3, 'Augustus', 'Code', 'augustus.code@northeastern.edu', 'x'),
    (1, 'Horton', 'Brumwell', 'horton.brumwell@northeastern.edu', 'x'),
    (1, 'Brandyn', 'Bonhome', 'brandyn.bonhome@northeastern.edu', 'x'),
    (1, 'Mercy', 'Dowry', 'mercy.dowry@northeastern.edu', 'x'),
    (1, 'Batholomew', 'De Freyne', 'batholomew.defreyne@northeastern.edu', 'x'),
    (1, 'Lindsey', 'Tysack', 'lindsey.tysack@northeastern.edu', 'x'), 
    (2, 'Darya', 'Brocket', 'darya.brocket@northeastern.edu', 'x'),
    (1, 'Tally', 'Weiner', 'tally.weiner@northeastern.edu', 'x'),
    (2, 'Matthew', 'Renfield', 'matthew.renfield@northeastern.edu', 'x'),
    (1, 'Aryn', 'Bydaway', 'aryn.bydaway@northeastern.edu', 'x'),
    (1, 'Farly', 'De la Perrelle', 'farly.delaperrelle@northeastern.edu', 'x'),
    (2, 'Maribelle', 'Codi', 'maribelle.codi@northeastern.edu', 'x'),
    (3, 'Irma', 'Root', 'irma.root@northeastern.edu', 'x'),
    (1, 'Sutherlan', 'MacKim', 'sutherlan.mackim@northeastern.edu', 'x'),
    (1, 'Damaris', 'Payfoot', 'damaris.payfoot@northeastern.edu', 'x'),
    (1, 'Holly-anne', 'Muscroft', 'holly-anne.muscroft@northeastern.edu', 'x'),
    (1, 'Griz', 'Nendick', 'griz.nendick@northeastern.edu', 'x'),
    (1, 'Zaria', 'Garralts', 'zaria.garralts@northeastern.edu', 'x'),
    (1, 'Carr', 'Dockerty', 'carr.dockerty@northeastern.edu', 'x'),
    (1, 'Hugh', 'Heibl', 'hugh.heibl@northeastern.edu', 'x'),
    (2, 'Naomi', 'Park', 'naomi.park@northeastern.edu', 'x'),
    (1, 'Ethan', 'Cho', 'ethan.cho@northeastern.edu', 'x'),
    (1, 'Mina', 'Lee', 'mina.lee@northeastern.edu', 'x'),
    (2, 'Kevin', 'Tran', 'kevin.tran@northeastern.edu', 'x'),
    (1, 'Sofia', 'Kim', 'sofia.kim@northeastern.edu', 'x'),
    (1, 'Daniel', 'Wu', 'daniel.wu@northeastern.edu', 'x');

-- categories students can filter by
INSERT INTO event_categories (category_name) VALUES
    ('Academic'),
    ('Career'),
    ('Social'),
    ('Sports'),
    ('Arts'),
    ('Networking'),
    ('Health'),
    ('Technology'),
    ('Entertainment'),
    ('Cultural'),
    ('Workshop');

-- rooms/venues on campus
INSERT INTO event_location (location_name, capacity) VALUES
    ('Curry Student Center Ballroom', 400),
    ('Snell Library Room 001',         60),
    ('ISEC Auditorium',               250),
    ('Cabot Quad',                    1000),
    ('Richards Hall Room 120',          80),
    ('West Village H Room 108',         70),
    ('Behrakis Health Sciences Center Room 215', 120),
    ('Shillman Hall Room 305',         100),
    ('Forsyth Building Room 201',       90),
    ('Ell Hall Auditorium',             200),
    ('Marino Recreation Center Gymnasium', 500),
    ('ISEC Room 102',                     75),
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
(14, 'Data Science Networking Night', '2026-05-22', '11:26:00', '17:04:00', 'upcoming', NULL, 'Connect with fellow students and professionals interested in data science and analytics.'),
(6, 'AI & Machine Learning Panel', '2026-06-26', '13:59:00', '15:06:00', 'upcoming', NULL, 'Join industry experts as they discuss the latest trends in artificial intelligence and machine learning.'),
(8, 'Resume & LinkedIn Workshop', '2026-04-29', '09:33:00', '13:10:00', 'upcoming', NULL, 'Improve your resume and LinkedIn profile with guidance from career advisors.'),
(16, 'Startup Founder Speaker Series', '2026-06-08', '12:35:00', '20:04', 'upcoming', NULL, 'Hear from startup founders about their journey and lessons learned in building a company.'),
(7, 'Finance Career Insights Session', '2026-06-24', '16:53:00', '21:12', 'upcoming', NULL, 'Learn about career paths and opportunities in finance from industry professionals.'),
(13, 'Tech Internship Info Session', '2026-05-16', '10:44:00', '17:15', 'upcoming', NULL, 'Get insights into securing internships in the tech industry and how to stand out.'),
(19, 'Women in STEM Networking Event', '2026-06-11', '15:23:00', '17:13', 'upcoming', NULL, 'Network with inspiring women in STEM fields and build meaningful connections.'),
(14, 'Cybersecurity Awareness Workshop', '2026-05-16', '09:10:00', '20:14', 'upcoming', NULL, 'Learn the fundamentals of cybersecurity and how to protect digital information.'),
(17, 'Product Management Crash Course', '2026-05-16', '16:36:00', '19:52', 'upcoming', NULL, 'A crash course on product management covering key skills and real-world applications.'),
(19, 'Consulting Case Prep Workshop', '2026-05-17', '09:49:00', '18:11', 'upcoming', NULL, 'Practice solving consulting case interviews and improve your problem-solving skills.'),
(12, 'Entrepreneurship Pitch Night', '2026-06-02', '15:43:00', '17:46', 'upcoming', NULL, 'Pitch your business ideas and receive feedback from peers and mentors.'),
(17, 'K-Pop Dance Showcase', '2026-06-15', '14:42', '17:39:00', 'upcoming', NULL, 'Enjoy performances of popular K-pop dances by student groups.'),
(17, 'Open Mic Night at Curry', '2026-05-22', '13:33', '15:56:00', 'upcoming', NULL, 'Showcase your talent or enjoy performances in a relaxed open mic setting.'),
(12, 'Spring Club Fair', '2026-05-27', '09:07:00', '15:40:00', 'upcoming', NULL, 'Discover different student organizations and get involved on campus.'),
(6, 'Mental Health & Wellness Seminar', '2026-06-16', '16:13:00', '19:24', 'upcoming', NULL, 'Learn strategies for maintaining mental health and overall wellness during college.'),
(5, 'Blockchain & FinTech Panel', '2026-05-18', '12:00:00', '14:00:00', 'upcoming', NULL, 'Explore the future of blockchain technology and its impact on finance.'),
(9, 'Global Culture Night', '2026-05-20', '18:00', '21:00:00', 'upcoming', NULL, 'Celebrate diverse cultures through performances, food, and activities.'),
(10, 'Basketball 3v3 Tournament', '2026-05-25', '10:00:00', '16:00:00', 'upcoming', NULL, 'Join a competitive 3v3 basketball tournament open to all students.'),
(11, 'UX/UI Design Workshop', '2026-05-21', '13:00:00', '16:00:00', 'upcoming', NULL, 'Learn the fundamentals of user experience and interface design.'),
(15, 'Volunteer Community Service Day', '2026-05-30', '09:00:00', '13:00:00', 'upcoming', NULL, 'Give back to the community through organized volunteer activities.'),
(18, 'Esports Tournament Finals', '2026-06-05', '17:00:00', '20:00:00', 'upcoming', NULL, 'Watch top student teams compete in the final round of the esports tournament.')
(3, 'Public Speaking Workshop', '2026-06-09', '15:00', '17:00', 'upcoming', NULL, 'Build confidence and presentation skills through interactive speaking exercises.'),
(9, 'International Student Mixer', '2026-06-12', '18:00', '20:30', 'upcoming', NULL, 'Meet students from around the world in a casual social setting with music and snacks.'),
(11, 'Volleyball Open Gym', '2026-06-14', '16:00', '19:00', 'upcoming', NULL, 'Join an open gym volleyball session for all skill levels.'),
(13, 'Women in Business Panel', '2026-06-18', '14:00', '16:00', 'upcoming', NULL, 'Hear from professionals and alumni about career growth and leadership in business.'),
(7, 'Photography Walk Around Boston', '2026-06-22', '10:00', '13:00', 'upcoming', NULL, 'Explore Boston while practicing photography techniques with fellow students.');

-- link each event to a category through the join table
INSERT INTO event_category_map (event_id, category_id) VALUES
    -- 1 Spring Career Fair 2026
    (1, 2), (1, 6), (1, 1), (1, 11), (1, 3),

    -- 2 CS3200 Study Jam
    (2, 1), (2, 11), (2, 3), (2, 8), (2, 7),

    -- 3 Student Film Screening
    (3, 5), (3, 9), (3, 10), (3, 3), (3, 1),

    -- 4 Intramural Soccer Tournament
    (4, 4), (4, 3), (4, 9), (4, 7), (4, 10),

    -- 5 Data Science Networking Night
    (5, 6), (5, 8), (5, 2), (5, 1), (5, 11), (5, 3),

    -- 6 AI & Machine Learning Panel
    (6, 8), (6, 1), (6, 2), (6, 11), (6, 6), (6, 9),

    -- 7 Resume & LinkedIn Workshop
    (7, 2), (7, 11), (7, 1), (7, 6), (7, 3),

    -- 8 Startup Founder Speaker Series
    (8, 2), (8, 6), (8, 11), (8, 1), (8, 8),

    -- 9 Finance Career Insights Session
    (9, 2), (9, 1), (9, 6), (9, 11), (9, 3),

    -- 10 Tech Internship Info Session
    (10, 2), (10, 8), (10, 6), (10, 11), (10, 1),

    -- 11 Women in STEM Networking Event
    (11, 6), (11, 8), (11, 2), (11, 1), (11, 10), (11, 3),

    -- 12 Cybersecurity Awareness Workshop
    (12, 8), (12, 11), (12, 1), (12, 2), (12, 6),

    -- 13 Product Management Crash Course
    (13, 2), (13, 11), (13, 8), (13, 1), (13, 6),

    -- 14 Consulting Case Prep Workshop
    (14, 2), (14, 11), (14, 1), (14, 6), (14, 3),

    -- 15 Entrepreneurship Pitch Night
    (15, 2), (15, 6), (15, 11), (15, 8), (15, 3), (15, 1),

    -- 16 K-Pop Dance Showcase
    (16, 5), (16, 9), (16, 10), (16, 3), (16, 7),

    -- 17 Open Mic Night at Curry
    (17, 5), (17, 9), (17, 3), (17, 10), (17, 6),

    -- 18 Spring Club Fair
    (18, 3), (18, 6), (18, 10), (18, 2), (18, 1),

    -- 19 Mental Health & Wellness Seminar
    (19, 7), (19, 11), (19, 1), (19, 3), (19, 6),

    -- 20 Blockchain & FinTech Panel
    (20, 8), (20, 2), (20, 1), (20, 6), (20, 11),

    -- 21 Global Culture Night
    (21, 10), (21, 3), (21, 5), (21, 9), (21, 6),

    -- 22 Basketball 3v3 Tournament
    (22, 4), (22, 3), (22, 7), (22, 9), (22, 6),

    -- 23 UX/UI Design Workshop
    (23, 8), (23, 11), (23, 1), (23, 2), (23, 5),

    -- 24 Volunteer Community Service Day
    (24, 3), (24, 10), (24, 6), (24, 1), (24, 11),

    -- 25 Esports Tournament Finals
    (25, 9), (25, 8), (25, 3), (25, 4), (25, 6), (25, 10)
    
    -- 26 Public Speaking Workshop
    (26, 11), (26, 1), (26, 3),

    -- 27 International Student Mixer
    (27, 3), (27, 10), (27, 6),

    -- 28 Volleyball Open Gym
    (28, 4), (28, 3), (28, 7),

    -- 29 Women in Business Panel
    (29, 2), (29, 6), (29, 1),

    -- 30 Photography Walk Around Boston
    (30, 5), (30, 3), (30, 10);

-- a couple of registrations so "My Events" isn't empty for user 1
INSERT INTO registration (event_id, user_id, status) VALUES
    (1, 1, 'registered'),
    (2, 1, 'registered'),
    (3, 2, 'registered'),
    (4, 6, 'registered'),
    (5, 9, 'registered'),
    (6, 10, 'registered'),
    (7, 12, 'registered'),
    (8, 15, 'registered'),
    (9, 18, 'registered'),
    (10, 21, 'registered'),
    (11, 24, 'registered'),
    (12, 2, 'registered'),
    (13, 6, 'registered'),
    (14, 9, 'registered'),
    (15, 10, 'registered'),
    (16, 12, 'registered'),
    (17, 15, 'registered'),
    (18, 18, 'registered'),
    (19, 21, 'registered'),
    (20, 24, 'registered'),
    (21, 1, 'registered'),
    (22, 2, 'registered'),
    (23, 6, 'registered'),
    (24, 9, 'registered'),
    (25, 10, 'registered'),
    (5, 1, 'registered'),
    (6, 2, 'registered'),
    (7, 9, 'registered'),
    (8, 10, 'registered'),
    (9, 12, 'registered'),
    (10, 15, 'registered'),
    (11, 18, 'registered'),
    (12, 21, 'registered'),
    (13, 24, 'registered'),
    (14, 1, 'registered'),
    (15, 2, 'registered'),
    (16, 6, 'registered'),
    (17, 9, 'registered'),
    (18, 10, 'registered'),
    (19, 12, 'registered'),
    (20, 15, 'registered'),
    (21, 18, 'registered'),
    (22, 21, 'registered'),
    (23, 24, 'registered'),
    (24, 1, 'cancelled'),
    (25, 2, 'cancelled'),
    (20, 6, 'cancelled'),
    (21, 10, 'cancelled'),
    (22, 15, 'cancelled'),
    (23, 18, 'cancelled');

-- one notification for the student to see
INSERT INTO notifications (user_id, event_id, message) VALUES
    (1, 1, 'Reminder: Spring Career Fair 2026 starts tomorrow at 10:00 AM.'),
    (1, 2, 'Reminder: CS3200 Study Jam starts tonight at 6:00 PM.'),
    (2, 3, 'You are registered for Student Film Screening.'),
    (6, 4, 'Reminder: Intramural Soccer Tournament starts this weekend.'),
    (9, 5, 'Data Science Networking Night is coming up soon.'),
    (10, 6, 'AI & Machine Learning Panel starts tomorrow afternoon.'),
    (12, 7, 'Your RSVP for Resume & LinkedIn Workshop is confirmed.'),
    (15, 8, 'Startup Founder Speaker Series has updated event details.'),
    (18, 9, 'Finance Career Insights Session is happening this week.'),
    (21, 10, 'Tech Internship Info Session starts tomorrow.'),
    (24, 11, 'Women in STEM Networking Event is almost here.'),
    (2, 12, 'Cybersecurity Awareness Workshop registration confirmed.'),
    (6, 13, 'Product Management Crash Course starts soon.'),
    (9, 14, 'Consulting Case Prep Workshop begins tomorrow morning.'),
    (10, 15, 'Entrepreneurship Pitch Night RSVP confirmed.'),
    (12, 16, 'K-Pop Dance Showcase starts this Friday.'),
    (15, 17, 'Open Mic Night at Curry is coming up soon.'),
    (18, 18, 'Spring Club Fair is tomorrow—check participating clubs.'),
    (21, 19, 'Mental Health & Wellness Seminar starts next week.'),
    (24, 20, 'Blockchain & FinTech Panel has open seats available.'),
    (1, 21, 'Global Culture Night starts tomorrow evening.'),
    (2, 22, 'Basketball 3v3 Tournament bracket information is now available.'),
    (6, 23, 'UX/UI Design Workshop reminder: bring your laptop.'),
    (9, 24, 'Volunteer Community Service Day check-in opens at 8:30 AM.'),
    (10, 25, 'Esports Tournament Finals begins at 5:00 PM.'),
    (2, 1, 'Spring Career Fair 2026 is one week away.'),
    (6, 5, 'New attendees have joined Data Science Networking Night.'),
    (9, 8, 'Startup Founder Speaker Series venue has been updated.'),
    (10, 10, 'Tech Internship Info Session has limited seats remaining.'),
    (12, 12, 'Cybersecurity Awareness Workshop starts in 24 hours.'),
    (15, 15, 'Entrepreneurship Pitch Night deadline to RSVP is today.'),
    (18, 16, 'K-Pop Dance Showcase starts in 2 days.'),
    (21, 18, 'Spring Club Fair map and schedule are now available.'),
    (24, 24, 'Volunteer Community Service Day RSVP confirmed.'),
    (1, 25, 'Esports Tournament Finals reminder sent successfully.'),
    (2, 5, 'Data Science Networking Night registration confirmed.'),
    (6, 6, 'AI & Machine Learning Panel starts at 1:59 PM.'),
    (9, 11, 'Women in STEM Networking Event reminder: check location details.'),
    (10, 13, 'Product Management Crash Course seats are filling quickly.'),
    (12, 14, 'Consulting Case Prep Workshop starts tomorrow.'),
    (15, 19, 'Mental Health & Wellness Seminar reminder sent.'),
    (18, 20, 'Blockchain & FinTech Panel starts next week.'),
    (21, 21, 'Global Culture Night features have been updated.'),
    (24, 22, 'Basketball 3v3 Tournament schedule has been posted.'),
    (1, 23, 'UX/UI Design Workshop reminder: bring a notebook.'),
    (2, 24, 'Volunteer Community Service Day location details have been shared.'),
    (6, 25, 'Esports Tournament Finals begins soon.'),
    (9, 17, 'Open Mic Night at Curry is accepting more performers.'),
    (10, 18, 'Spring Club Fair RSVP confirmed.'),
    (12, 20, 'Blockchain & FinTech Panel RSVP confirmed.');


INSERT INTO attendance (user_id, event_id, attendance_status) VALUES
    (1, 1, 'checked_in'),
    (1, 2, 'checked_in'),
    (2, 3, 'checked_in'),

    (6, 4, 'checked_in'),
    (9, 5, 'checked_in'),
    (10, 6, 'checked_in'),
    (12, 7, 'checked_in'),
    (15, 8, 'checked_in'),
    (18, 9, 'checked_in'),
    (21, 10, 'checked_in'),

    (24, 11, 'checked_in'),
    (2, 12, 'checked_in'),
    (6, 13, 'checked_in'),
    (9, 14, 'checked_in'),
    (10, 15, 'checked_in'),
    (12, 16, 'checked_in'),

    (15, 17, 'checked_in'),
    (18, 18, 'checked_in'),
    (21, 19, 'checked_in'),
    (24, 20, 'checked_in'),

    (1, 21, 'checked_in'),
    (2, 22, 'checked_in'),
    (6, 23, 'checked_in'),
    (9, 24, 'checked_in'),

    (1, 5, 'checked_in'),
    (2, 6, 'checked_in'),
    (9, 7, 'checked_in'),
    (10, 8, 'checked_in'),
    (12, 9, 'checked_in'),
    (15, 10, 'checked_in'),

    (18, 11, 'checked_in'),
    (21, 12, 'checked_in'),
    (24, 13, 'checked_in'),
    (1, 14, 'checked_in'),
    (2, 15, 'checked_in')
    
    (25, 26, 'checked_in'),
    (26, 27, 'checked_in'),
    (27, 28, 'checked_in'),
    (28, 29, 'checked_in'),
    (29, 30, 'checked_in'),
    (30, 26, 'checked_in'),
    (25, 27, 'checked_in'),
    (26, 28, 'checked_in'),
    (27, 29, 'checked_in'),
    (28, 30, 'checked_in'),
    (29, 26, 'checked_in'),
    (30, 27, 'checked_in'),
    (25, 28, 'checked_in'),
    (26, 29, 'checked_in'),
    (27, 30, 'checked_in');

INSERT INTO waitlist (event_id, user_id, queued_pos, status) VALUES
    (5, 2, 1, 'waiting'),
    (5, 6, 2, 'waiting'),
    (6, 9, 1, 'promoted'),
    (7, 10, 1, 'waiting'),
    (8, 12, 1, 'waiting'),
    (9, 15, 1, 'expired'),
    (10, 18, 1, 'waiting'),
    (11, 21, 1, 'promoted'),
    (12, 24, 1, 'waiting'),
    (13, 1, 1, 'waiting'),
    (14, 2, 1, 'waiting'),
    (15, 6, 1, 'promoted'),
    (16, 9, 1, 'waiting'),
    (17, 10, 1, 'waiting'),
    (18, 12, 1, 'expired'),
    (19, 15, 1, 'waiting'),
    (20, 18, 1, 'waiting'),
    (21, 21, 1, 'promoted')
    (26, 28, 1, 'waiting'),
    (26, 29, 2, 'waiting'),
    (27, 30, 1, 'promoted'),
    (27, 25, 2, 'waiting'),
    (28, 26, 1, 'waiting'),
    (28, 27, 2, 'expired'),
    (29, 30, 1, 'waiting'),
    (29, 25, 2, 'promoted'),
    (30, 26, 1, 'waiting'),
    (30, 27, 2, 'waiting');


INSERT INTO event_views (event_id, user_id) VALUES
    (1, 1), (1, 2), (1, 6), (1, 9), (1, 10),
    (2, 1), (2, 2), (2, 12), (2, 15), (2, 18),
    (3, 2), (3, 6), (3, 9), (3, 21), (3, 24),
    (4, 1), (4, 10), (4, 12), (4, 15), (4, 18),
    (5, 1), (5, 2), (5, 6), (5, 9), (5, 10),
    (5, 12), (5, 15), (5, 18), (5, 21), (5, 24),
    (6, 1), (6, 2), (6, 6), (6, 9), (6, 10),
    (6, 12), (6, 15), (6, 18), (6, 21), (6, 24),
    (7, 1), (7, 2), (7, 6), (7, 9), (7, 10),
    (8, 2), (8, 6), (8, 9), (8, 10), (8, 12),
    (8, 15), (8, 18), (8, 21), (8, 24),
    (9, 1), (9, 2), (9, 6), (9, 9), (9, 10),
    (10, 1), (10, 2), (10, 6), (10, 9), (10, 10),
    (10, 12), (10, 15), (10, 18),
    (11, 1), (11, 2), (11, 6), (11, 9), (11, 10),
    (11, 12), (11, 15), (11, 18), (11, 21),
    (12, 1), (12, 2), (12, 6), (12, 9), (12, 10),
    (12, 12), (12, 15),
    (13, 1), (13, 2), (13, 6), (13, 9), (13, 10),
    (13, 12), (13, 15), (13, 18),
    (14, 2), (14, 6), (14, 9), (14, 10), (14, 12),
    (14, 15), (14, 18),
    (15, 1), (15, 2), (15, 6), (15, 9), (15, 10),
    (15, 12), (15, 15), (15, 18), (15, 21),
    (16, 1), (16, 2), (16, 6), (16, 9), (16, 10),
    (16, 12), (16, 15), (16, 18), (16, 21), (16, 24),
    (17, 1), (17, 2), (17, 6), (17, 9), (17, 10),
    (17, 12), (17, 15), (17, 18), (17, 21),
    (18, 1), (18, 2), (18, 6), (18, 9), (18, 10),
    (18, 12), (18, 15), (18, 18), (18, 21), (18, 24),
    (19, 1), (19, 2), (19, 6), (19, 9), (19, 10),
    (19, 12), (19, 15), (19, 18),
    (20, 1), (20, 2), (20, 6), (20, 9), (20, 10),
    (21, 1), (21, 2), (21, 6), (21, 9), (21, 10),
    (21, 12), (21, 15), (21, 18), (21, 21),
    (22, 1), (22, 2), (22, 6), (22, 9), (22, 10),
    (22, 12), (22, 15), (22, 18),
    (23, 1), (23, 2), (23, 6), (23, 9), (23, 10),
    (23, 12), (23, 15),
    (24, 1), (24, 2), (24, 6), (24, 9), (24, 10),
    (24, 12), (24, 15), (24, 18), (24, 21),
    (25, 1), (25, 2), (25, 6), (25, 9), (25, 10),
    (25, 12), (25, 15), (25, 18), (25, 21), (25, 24);

INSERT INTO comments (user_id, event_id, comment_text, status) VALUES
    (2, 1, 'Will there be a list of participating companies posted beforehand?', 'visible'),
    (6, 1, 'Really excited for this one.', 'visible'),
    (9, 2, 'Can someone share what topics will be covered?', 'visible'),
    (10, 2, 'Looking forward to studying with everyone.', 'visible'),
    (12, 3, 'Do we need tickets for the screening?', 'visible'),
    (15, 3, 'This sounds like a fun event.', 'visible'),
    (18, 4, 'Can beginners join the tournament?', 'visible'),
    (21, 5, 'Is this event open to first-year students too?', 'visible'),
    (24, 5, 'This seems like a great networking opportunity.', 'visible'),
    (1, 6, 'Will the panel include time for questions?', 'visible'),
    (2, 6, 'I hope they talk about career paths too.', 'visible'),
    (6, 7, 'Can alumni attend this workshop?', 'visible'),
    (9, 8, 'Excited to hear from startup founders.', 'visible'),
    (10, 8, 'This should be really informative.', 'visible'),
    (12, 9, 'Will there be finance recruiters there?', 'visible'),
    (15, 10, 'I have been waiting for an event like this.', 'visible'),
    (18, 11, 'Love seeing more events like this on campus.', 'visible'),
    (21, 12, 'Will slides or materials be shared afterward?', 'visible'),
    (24, 13, 'This fits perfectly with my interests.', 'visible'),
    (1, 14, 'Case prep is exactly what I need right now.', 'visible'),
    (2, 15, 'Can we attend even if we are not pitching?', 'visible'),
    (6, 16, 'Can’t wait to watch the performances.', 'visible'),
    (9, 17, 'Do we need to sign up in advance to perform?', 'visible'),
    (10, 18, 'This is a good chance to meet more clubs.', 'visible'),
    (12, 19, 'Really glad the app includes wellness events too.', 'visible'),
    (15, 20, 'This topic sounds super relevant right now.', 'visible'),
    (18, 21, 'Looking forward to the food and performances.', 'visible'),
    (21, 22, 'Can teams sign up on the day of the tournament?', 'visible'),
    (24, 23, 'UI/UX is such a useful skill to learn.', 'visible'),
    (1, 24, 'Happy to see community service opportunities included.', 'visible'),
    (2, 25, 'This final is going to be intense.', 'visible')
    (25, 26, 'This workshop sounds really useful.', 'visible'),
    (26, 26, 'Will there be time for practice speeches?', 'visible'),
    (27, 27, 'This sounds like a great way to meet new people.', 'visible'),
    (28, 27, 'Are snacks provided at the mixer?', 'visible'),
    (29, 28, 'Can beginners join the open gym?', 'visible'),
    (30, 28, 'Looking forward to this event.', 'visible'),
    (25, 29, 'Excited to hear from the panelists.', 'visible'),
    (26, 29, 'Will alumni be there for networking after?', 'visible'),
    (27, 30, 'This event sounds really creative.', 'visible'),
    (28, 30, 'Do we need to bring our own camera?', 'visible'),
    (29, 26, 'I need this before my next class presentation.', 'visible'),
    (30, 27, 'Love that the app includes events like this.', 'visible'),
    (25, 28, 'Hope there is enough space for everyone.', 'visible'),
    (26, 29, 'This is exactly the kind of event I was looking for.', 'visible'),
    (27, 30, 'Boston is a great place for a photo walk.', 'visible'),
    (28, 26, 'Can non-native English speakers join too?', 'visible'),
    (29, 27, 'This should be a fun social event.', 'visible'),
    (30, 28, 'Would be great if teams rotate often.', 'visible'),
    (25, 29, 'Really glad to see more business events on here.', 'visible');

INSERT INTO event_history (user_id, event_id, feedback_rating) VALUES
    (6, 4, 4),
    (9, 5, 5),
    (10, 6, 4),
    (12, 7, 5),
    (15, 8, 4),
    (18, 9, 4),
    (21, 10, 5),
    (24, 11, 5),
    (2, 12, 4),
    (6, 13, 5),
    (9, 14, 4),
    (10, 15, 5),
    (12, 16, 4),
    (15, 17, 4),
    (18, 18, 5),
    (21, 19, 5),
    (24, 20, 4),
    (1, 21, 5),
    (2, 22, 4),
    (6, 23, 5),
    (9, 24, 5),
    (10, 25, 4),
    (12, 10, 3),
    (15, 5, 4),
    (18, 6, 5),
    (21, 15, 4),
    (24, 18, 5),
    (1, 20, 4),
    (2, 21, 5),
    (6, 22, 4)
    (25, 26, 5),
    (26, 27, 4),
    (27, 28, 4),
    (28, 29, 5),
    (29, 30, 5),
    (30, 26, 4),
    (25, 27, 5),
    (26, 28, 4),
    (27, 29, 5),
    (28, 30, 4),
    (29, 26, 4),
    (30, 27, 5),
    (25, 28, 3),
    (26, 29, 5),
    (27, 30, 4),
    (28, 26, 5),
    (29, 27, 4),
    (30, 28, 4),
    (25, 29, 5),
    (26, 30, 4);

INSERT INTO logs (user_id, action_type, description) VALUES
    (3, 'update_event', 'Updated event details for Student Film Screening'),
    (3, 'send_notification', 'Sent reminder for Spring Career Fair 2026'),
    (4, 'view_dashboard', 'Viewed event performance dashboard'),
    (3, 'create_event', 'Created Data Science Networking Night'),
    (3, 'create_event', 'Created AI & Machine Learning Panel'),
    (3, 'create_event', 'Created Resume & LinkedIn Workshop'),
    (4, 'backup_check', 'Reviewed nightly backup status'),
    (3, 'update_event', 'Changed location for Startup Founder Speaker Series'),
    (4, 'role_review', 'Reviewed user role assignments'),
    (3, 'send_notification', 'Sent update for Finance Career Insights Session'),
    (4, 'view_logs', 'Inspected recent platform activity'),
    (3, 'update_event', 'Updated description for Tech Internship Info Session'),
    (3, 'send_notification', 'Sent reminder for Women in STEM Networking Event'),
    (4, 'moderate_comment', 'Reviewed comment flagged as inappropriate'),
    (3, 'create_event', 'Created Blockchain & FinTech Panel'),
    (3, 'create_event', 'Created Global Culture Night'),
    (3, 'create_event', 'Created Basketball 3v3 Tournament'),
    (3, 'create_event', 'Created UX/UI Design Workshop'),
    (3, 'create_event', 'Created Volunteer Community Service Day'),
    (3, 'create_event', 'Created Esports Tournament Finals')
    (3, 'create_event', 'Created Public Speaking Workshop'),
    (3, 'create_event', 'Created International Student Mixer'),
    (3, 'create_event', 'Created Volleyball Open Gym'),
    (3, 'create_event', 'Created Women in Business Panel'),
    (3, 'create_event', 'Created Photography Walk Around Boston'),
    (4, 'view_dashboard', 'Reviewed dashboard metrics for upcoming events'),
    (3, 'send_notification', 'Sent reminder for Public Speaking Workshop'),
    (3, 'send_notification', 'Sent reminder for International Student Mixer'),
    (3, 'update_event', 'Updated description for Women in Business Panel'),
    (4, 'backup_check', 'Confirmed latest backup completed successfully'),
    (3, 'update_event', 'Adjusted time for Volleyball Open Gym'),
    (4, 'view_logs', 'Reviewed application activity log'),
    (3, 'send_notification', 'Sent reminder for Photography Walk Around Boston'),
    (4, 'role_review', 'Reviewed permissions for event coordinators'),
    (3, 'update_event', 'Updated venue details for International Student Mixer');

INSERT INTO backups (user_id, status) VALUES
    (4, 'completed'),
    (4, 'completed'),
    (4, 'completed'),
    (4, 'failed'),
    (4, 'completed'),
    (4, 'in_progress'),
    (4, 'completed'),
    (4, 'completed'),
    (4, 'failed')
    (4, 'completed'),
    (4, 'completed'),
    (4, 'completed'),
    (4, 'failed'),
    (4, 'completed'),
    (4, 'completed'),
    (4, 'in_progress'),
    (4, 'completed'),
    (4, 'completed'),
    (4, 'failed');
