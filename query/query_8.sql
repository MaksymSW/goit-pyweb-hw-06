--Знайти середній бал, який ставить певний викладач зі своїх предметів

SELECT t.name AS teacher_name, sub.name AS subjects_name, AVG(g.grade) AS average_grade
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
JOIN teachers t ON sub.teacher_id = t.id
GROUP BY t.id;