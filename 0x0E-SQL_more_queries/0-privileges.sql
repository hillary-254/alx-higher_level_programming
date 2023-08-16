-- List all privileges of users user_0d_1 and user_0d_2 on localhost

-- Create user user_0d_1
CREATE USER 'user_0d_1'@'localhost';

-- Grant privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Load privileges for user_0d_1
SELECT * FROM mysql.user WHERE user='user_0d_1' AND host='localhost';

-- Create user user_0d_2
CREATE USER 'user_0d_2'@'localhost';

-- Error: No privileges defined for user_0d_2
