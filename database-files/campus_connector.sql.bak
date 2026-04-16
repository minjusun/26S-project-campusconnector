DROP DATABASE IF EXISTS campus_connector;
CREATE DATABASE campus_connector;
USE campus_connector;

DROP TABLE IF EXISTS event_category_map;
DROP TABLE IF EXISTS event_history;
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS waitlist;
DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS registration;
DROP TABLE IF EXISTS logs;
DROP TABLE IF EXISTS event_views;
DROP TABLE IF EXISTS notifications;
DROP TABLE IF EXISTS backups;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS event_location;
DROP TABLE IF EXISTS event_categories;
DROP TABLE IF EXISTS user_roles;

CREATE TABLE user_roles (
    role_id INT AUTO_INCREMENT,
    role_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (role_id)
);

CREATE TABLE event_categories (
    category_id INT AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (category_id)
);

CREATE TABLE event_location (
    location_id INT AUTO_INCREMENT,
    capacity INT NOT NULL,
    PRIMARY KEY (location_id)
);

CREATE TABLE users (
    user_id INT AUTO_INCREMENT,
    role_id INT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    status VARCHAR(20) NOT NULL DEFAULT 'active',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    password_hash VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_id),
    CONSTRAINT fk_users_role
        FOREIGN KEY (role_id) REFERENCES user_roles (role_id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE events (
    event_id INT AUTO_INCREMENT,
    category_id INT NOT NULL,
    location_id INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status VARCHAR(20) NOT NULL,
    image_url VARCHAR(500),
    description TEXT,
    PRIMARY KEY (event_id),
    CONSTRAINT fk_events_category
        FOREIGN KEY (category_id) REFERENCES event_categories (category_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_events_location
        FOREIGN KEY (location_id) REFERENCES event_location (location_id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE event_category_map (
    event_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (event_id, category_id),
    CONSTRAINT fk_ecm_event
        FOREIGN KEY (event_id) REFERENCES events (event_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_ecm_category
        FOREIGN KEY (category_id) REFERENCES event_categories (category_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE backups (
    backup_id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    backup_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL,
    PRIMARY KEY (backup_id),
    CONSTRAINT fk_backups_user
        FOREIGN KEY (user_id) REFERENCES users (user_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE notifications (
    notification_id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    event_id INT NOT NULL,
    message TEXT NOT NULL,
    sent_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (notification_id),
    CONSTRAINT fk_notifications_user
        FOREIGN KEY (user_id) REFERENCES users (user_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_notifications_event
        FOREIGN KEY (event_id) REFERENCES events (event_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE event_views (
    view_id INT AUTO_INCREMENT,
    event_id INT NOT NULL,
    user_id INT NOT NULL,
    viewed_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (view_id),
    CONSTRAINT fk_event_views_event
        FOREIGN KEY (event_id) REFERENCES events (event_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_event_views_user
        FOREIGN KEY (user_id) REFERENCES users (user_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE logs (
    log_id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    action_type VARCHAR(50) NOT NULL,
    description TEXT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (log_id),
    CONSTRAINT fk_logs_user
        FOREIGN KEY (user_id) REFERENCES users (user_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE registration (
    registration_id INT AUTO_INCREMENT,
    event_id INT NOT NULL,
    user_id INT NOT NULL,
    status VARCHAR(20) NOT NULL,
    registered_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (registration_id),
    CONSTRAINT fk_registration_event
        FOREIGN KEY (event_id) REFERENCES events (event_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_registration_user
        FOREIGN KEY (user_id) REFERENCES users (user_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    event_id INT NOT NULL,
    attendance_status VARCHAR(20) NOT NULL,
    check_in_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (attendance_id),
    CONSTRAINT fk_attendance_user
        FOREIGN KEY (user_id) REFERENCES users (user_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_attendance_event
        FOREIGN KEY (event_id) REFERENCES events (event_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE waitlist (
    waitlist_id INT AUTO_INCREMENT,
    event_id INT NOT NULL,
    user_id INT NOT NULL,
    queued_pos INT NOT NULL,
    status VARCHAR(20) NOT NULL,
    joined_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    notified_at DATETIME,
    PRIMARY KEY (waitlist_id),
    CONSTRAINT fk_waitlist_event
        FOREIGN KEY (event_id) REFERENCES events (event_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_waitlist_user
        FOREIGN KEY (user_id) REFERENCES users (user_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE comments (
    comment_id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    event_id INT NOT NULL,
    comment_text TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL,
    PRIMARY KEY (comment_id),
    CONSTRAINT fk_comments_user
        FOREIGN KEY (user_id) REFERENCES users (user_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_comments_event
        FOREIGN KEY (event_id) REFERENCES events (event_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE event_history (
    history_id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    event_id INT NOT NULL,
    attended_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    feedback_rating INT,
    PRIMARY KEY (history_id),
    CONSTRAINT fk_event_history_user
        FOREIGN KEY (user_id) REFERENCES users (user_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_event_history_event
        FOREIGN KEY (event_id) REFERENCES events (event_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO user_roles (role_id, role_name) VALUES
(10, 'student'),
(11, 'event_manager'),
(12, 'administrator'),
(13, 'moderator'),
(14, 'guest');

INSERT INTO event_categories (category_id, category_name) VALUES
(10, 'Academic'),
(11, 'Social'),
(12, 'Sports'),
(13, 'Career'),
(14, 'Arts');

INSERT INTO event_location (location_id, capacity) VALUES
(10, 200),
(11, 50),
(12, 500),
(13, 100),
(14, 30);

INSERT INTO users (user_id, role_id, first_name, last_name, email, status, password_hash) VALUES
(10, 10, 'Alex', 'Johnson', 'johnson.al@northeastern.edu', 'active', 'hashed_pw_001'),
(11, 11, 'Maria', 'Chen', 'chen.ma@northeastern.edu', 'active', 'hashed_pw_002'),
(12, 12, 'James', 'Smith', 'smith.ja@northeastern.edu', 'active', 'hashed_pw_003'),
(13, 10, 'Priya', 'Patel', 'patel.pr@northeastern.edu', 'active', 'hashed_pw_004'),
(14, 13, 'Tyler', 'Brooks', 'brooks.ty@northeastern.edu', 'active', 'hashed_pw_005');

INSERT INTO events (event_id, category_id, location_id, title, date, start_time, end_time, status, image_url, description) VALUES
(10, 10, 10, 'CS Study Session', '2026-04-10', '14:00:00', '16:00:00', 'upcoming', NULL, 'Group study session for CS3200 midterm prep.'),
(11, 11, 11, 'Spring Social Mixer', '2026-04-12', '18:00:00', '21:00:00', 'upcoming', NULL, 'Meet fellow students at a casual social event.'),
(12, 12, 12, 'Intramural Soccer Finals', '2026-04-15', '17:00:00', '19:00:00', 'upcoming', NULL, 'Championship game for intramural soccer league.'),
(13, 13, 13, 'Resume Workshop', '2026-04-18', '12:00:00', '13:30:00', 'upcoming', NULL, 'Get your resume reviewed by industry professionals.'),
(14, 14, 14, 'Open Mic Night', '2026-04-20', '19:00:00', '22:00:00', 'upcoming', NULL, 'Perform poetry, music, or comedy on stage.');

INSERT INTO event_category_map (event_id, category_id) VALUES
(10, 10),
(11, 11),
(12, 12),
(13, 13),
(14, 14);

INSERT INTO backups (backup_id, user_id, backup_time, status) VALUES
(10, 12, '2026-04-01 02:00:00', 'completed'),
(11, 12, '2026-04-02 02:00:00', 'completed'),
(12, 12, '2026-04-03 02:00:00', 'failed'),
(13, 12, '2026-04-04 02:00:00', 'completed'),
(14, 12, '2026-04-05 02:00:00', 'in_progress');

INSERT INTO notifications (notification_id, user_id, event_id, message, sent_at) VALUES
(10, 10, 10, 'Reminder: CS Study Session is tomorrow!', '2026-04-09 10:00:00'),
(11, 10, 11, 'You are registered for Spring Social Mixer.', '2026-04-10 12:00:00'),
(12, 13, 12, 'Intramural Soccer Finals is this week!', '2026-04-13 09:00:00'),
(13, 14, 13, 'Resume Workshop spots are filling up.', '2026-04-16 08:00:00'),
(14, 13, 14, 'Open Mic Night is this Friday!', '2026-04-18 10:00:00');

INSERT INTO event_views (view_id, event_id, user_id, viewed_at) VALUES
(10, 10, 10, '2026-04-05 09:30:00'),
(11, 11, 10, '2026-04-06 11:00:00'),
(12, 12, 12, '2026-04-07 15:45:00'),
(13, 13, 13, '2026-04-08 14:20:00'),
(14, 14, 14, '2026-04-09 18:00:00');

INSERT INTO logs (log_id, user_id, action_type, description, created_at) VALUES
(10, 11, 'create_event', 'Created event: CS Study Session', '2026-04-01 10:00:00'),
(11, 12, 'update_role', 'Changed user 11 role to event_manager', '2026-04-01 09:00:00'),
(12, 11, 'create_event', 'Created event: Spring Social Mixer', '2026-04-02 11:00:00'),
(13, 12, 'delete_user', 'Removed inactive user account', '2026-04-03 15:00:00'),
(14, 14, 'moderate_comment', 'Flagged inappropriate comment', '2026-04-04 16:30:00');

INSERT INTO registration (registration_id, event_id, user_id, status, registered_at) VALUES
(10, 10, 10, 'registered', '2026-04-05 10:00:00'),
(11, 11, 10, 'registered', '2026-04-06 11:30:00'),
(12, 12, 12, 'registered', '2026-04-07 16:00:00'),
(13, 13, 13, 'registered', '2026-04-08 09:00:00'),
(14, 14, 14, 'cancelled', '2026-04-09 20:00:00');

INSERT INTO attendance (attendance_id, user_id, event_id, attendance_status, check_in_time) VALUES
(10, 10, 10, 'checked_in', '2026-04-10 14:05:00'),
(11, 12, 12, 'checked_in', '2026-04-15 16:55:00'),
(12, 13, 10, 'checked_in', '2026-04-10 14:10:00'),
(13, 13, 13, 'no_show', '2026-04-18 12:00:00'),
(14, 14, 14, 'checked_in', '2026-04-20 19:05:00');

INSERT INTO waitlist (waitlist_id, event_id, user_id, queued_pos, status, joined_at, notified_at) VALUES
(10, 11, 12, 1, 'waiting', '2026-04-11 08:00:00', NULL),
(11, 10, 11, 1, 'promoted', '2026-04-08 09:00:00', '2026-04-09 09:00:00'),
(12, 13, 10, 2, 'waiting', '2026-04-16 10:00:00', NULL),
(13, 14, 12, 1, 'waiting', '2026-04-19 12:00:00', NULL),
(14, 11, 14, 2, 'expired', '2026-04-11 09:00:00', '2026-04-11 17:00:00');

INSERT INTO comments (comment_id, user_id, event_id, comment_text, created_at, updated_at, status) VALUES
(10, 10, 10, 'Looking forward to this study session!', '2026-04-06 14:00:00', '2026-04-06 14:00:00', 'visible'),
(11, 12, 12, 'Who else is coming to the finals?', '2026-04-08 10:00:00', '2026-04-08 10:00:00', 'visible'),
(12, 13, 11, 'Can we bring friends who arent registered?', '2026-04-10 15:00:00', '2026-04-10 15:00:00', 'visible'),
(13, 14, 13, 'Will there be recruiters from tech companies?', '2026-04-15 11:00:00', '2026-04-15 11:00:00', 'visible'),
(14, 10, 14, 'Im signing up to perform a song!', '2026-04-17 20:00:00', '2026-04-17 20:00:00', 'hidden');

INSERT INTO event_history (history_id, user_id, event_id, attended_at, feedback_rating) VALUES
(10, 10, 10, '2026-04-10 16:00:00', 5),
(11, 12, 12, '2026-04-15 19:00:00', 4),
(12, 13, 10, '2026-04-10 16:00:00', 3),
(13, 13, 13, '2026-04-18 13:30:00', 5),
(14, 14, 14, '2026-04-20 22:00:00', 4);