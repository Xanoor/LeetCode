--197
SELECT w.id FROM Weather w, Weather w2 WHERE w.temperature>w2.temperature AND DATE_SUB(w.recordDate, INTERVAL 1 DAY) = w2.recordDate;

--OR
SELECT id FROM Weather w WHERE temperature>(SELECT temperature FROM Weather w2 WHERE DATE_SUB(w.recordDate, INTERVAL 1 DAY) = w2.recordDate);

--OR
SELECT w.id FROM Weather w, Weather w2 WHERE w.temperature>w2.temperature AND DATEDIFF(w.recordDate, w2.recordDATE) = 1;