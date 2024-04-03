-- Write your PostgreSQL query statement below
SELECT email 
FROM person
GROUP BY email
HAVING count(1) > 1
;