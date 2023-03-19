--# --| 1 |-- #--
SELECT COUNT(*) FROM etudiants WHERE 18 <= age AND age <= 25;
--# --| 2 |-- #--
SELECT COUNT(*) FROM etudiants WHERE age BETWEEN 18 and 25;