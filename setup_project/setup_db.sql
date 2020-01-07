CREATE DATABASE iw_db;
CREATE USER 'iw_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON iw_db.* TO 'iw_user'@'localhost';
