-- Create database hbtn_0d_2 and user user_0d_2 with SELECT privilege

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user user_0d_2 if not exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant privileges to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Load privileges for user_0d_1 and user_0d_2
SELECT * FROM mysql.user WHERE user IN ('user_0d_1', 'user_0d_2') AND host='localhost';
SELECT * FROM mysql.db WHERE user IN ('user_0d_1', 'user_0d_2') AND db='hbtn_0d_2';
