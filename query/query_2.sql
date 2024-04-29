--Знайти студента із найвищим середнім балом з французського.

SELECT s.name, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.name = 'French'
GROUP BY s.id
ORDER BY AVG(g.grade) DESC
LIMIT 1;