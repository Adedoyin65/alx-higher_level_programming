-- create_table.sql
-- Script to create MySQL table force_name

-- Create table if not exists
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
