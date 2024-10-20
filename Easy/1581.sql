--1581
SELECT customer_id, COUNT(DISTINCT Visits.visit_id) count_no_trans FROM Visits, Transactions WHERE Visits.visit_id NOT IN (SELECT visit_id FROM Transactions)  GROUP BY customer_id;