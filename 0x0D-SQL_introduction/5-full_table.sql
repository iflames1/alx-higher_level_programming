-- script that prints the full description of the table first_table from
-- the database hbtn_0c_0 in your MySQL server.
SELECT TABLE_NAME, COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT
FROM information_schema.columns
WHERE table_schema = DATABASE() AND table_name = 'first_table';
