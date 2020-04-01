/*
This script creates the hbnt_dev_db database if it does not exist,
also creates the user hbnb_dev if it does not exist,
all privileges are granted to the user for the hbnt_dev_db database,
finally you are granted the SELECT permission on the performance_schema database
*/
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
