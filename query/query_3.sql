--Знайти середній бал у групах з италийського

SELECT g.subject_id ,gr.name, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
JOIN students s ON g.student_id = s.id
JOIN groups gr ON s.group_id = gr.id
WHERE sub.name = 'Italian'
GROUP BY gr.id;