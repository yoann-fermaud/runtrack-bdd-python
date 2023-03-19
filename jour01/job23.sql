--# --| 1 |-- #--
SELECT * FROM etudiants WHERE age = (SELECT MAX(age) FROM etudiants);
--# --| 2 |-- #--
SELECT * FROM etudiants ORDER BY age DESC LIMIT 1;