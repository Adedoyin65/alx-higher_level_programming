-- A script that prints the full description of the
-- table first_table from the database hbtn_0c_0 in your MySQL server.
SELECT column_name, data_type, character_maximum_length, is_nullable, column_default, column_key, extra, column_comment
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
