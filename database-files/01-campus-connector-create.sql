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
    location_name VARCHAR(100) NOT NULL,
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
    location_id INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status VARCHAR(20) NOT NULL,
    image_url VARCHAR(500),
    description TEXT,
    PRIMARY KEY (event_id),
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