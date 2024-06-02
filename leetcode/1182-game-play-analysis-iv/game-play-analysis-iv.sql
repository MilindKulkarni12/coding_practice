-- Write your PostgreSQL query statement below

-- SELECT x.player_id, x.event_date,
SELECT ROUND((SUM(CASE WHEN a.event_date - x.event_date = 1 THEN 1 ELSE 0 END)::FLOAT / COUNT(DISTINCT a.player_id)::FLOAT)::NUMERIC, 2) AS fraction
FROM (
    SELECT player_id, event_date, RANK() OVER (PARTITION BY player_id ORDER BY event_date) as rk
    FROM activity
) x
JOIN activity a 
    ON a.player_id = x.player_id
WHERE x.rk = 1 
-- AND a.event_date - x.event_date = 1
;
