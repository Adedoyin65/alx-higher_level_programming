-- create_id_not_null_table.sql
-- Script to create MySQL table id_not_null

-- Create table if not exists
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
