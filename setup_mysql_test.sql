-- Creates A DataBase and a Test User
-- a new user hbnb_test in localhost
-- grants all privileges to the user on the hbnb_test_db database
-- grants SELECT privelege on the performance_schema database

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
