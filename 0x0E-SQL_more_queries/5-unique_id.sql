-- create_unique_id_table.sql
-- Script to create MySQL table unique_id

-- Create table if not exists
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
