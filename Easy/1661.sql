--1661
SELECT machine_id, ROUND((SUM(tm)/COUNT(tm)), 3) AS processing_time FROM (SELECT machine_id, MAX(timestamp)-MIN(timestamp) AS tm FROM Activity GROUP BY machine_id, process_id) AS tb GROUP BY machine_id;