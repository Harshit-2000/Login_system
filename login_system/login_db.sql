CREATE DATABASE login_db;

CREATE TABLE users(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(100) NOT NULL UNIQUE,
pass VARCHAR(255) NOT NULL,
created_at TIMESTAMP DEFAULT NOW()
);

DESC users;

INSERT INTO users(username, pass) VALUES 
('user1', 'password123');

SELECT * FROM users;


