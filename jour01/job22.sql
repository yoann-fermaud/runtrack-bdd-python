--# --| 1 |-- #--
SELECT * FROM etudiants WHERE age = (SELECT MIN(age) FROM etudiants);
--# --| 2 |-- #--
SELECT * FROM etudiants ORDER BY age ASC LIMIT 1;