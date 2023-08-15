-- Lists all records of table `second_table`
-- of the db `hbtn_0c_0` in MySQL Server.

SELECT score, name
FROM second_table
WHERE `name` IS NOT NULL
ORDER BY score DESC;
