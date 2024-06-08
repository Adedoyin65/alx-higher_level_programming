-- create_user.sql
-- Script to create MySQL user user_0d_1 with all privileges

-- Check if user_0d_1 exists
SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = user_0d_1 AND host = localhost) INTO @user_exists;

-- Create user if not exists
SET @create_user_query = IF(@user_exists, SELECT User already exists, CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd');
PREPARE stmt FROM @create_user_query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;

-- Apply the changes
FLUSH PRIVILEGES;
