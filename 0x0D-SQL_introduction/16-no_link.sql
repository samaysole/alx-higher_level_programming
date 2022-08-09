-- a script that lists all records of the table second_table
-- Don’t list rows without a name value
-- Results should display the score and the name
-- Records should be listed by descending score
SELECT score, name FROM second_table 
HAVING name IS NOT NULL ORDER BY score DESC;