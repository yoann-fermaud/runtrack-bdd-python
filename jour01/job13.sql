--# --| 1 |-- #--
SELECT * FROM etudiants WHERE 18 <= age AND age <= 25;
--# --| 2 |-- #--
SELECT * FROM etudiants WHERE age BETWEEN 18 and 25;