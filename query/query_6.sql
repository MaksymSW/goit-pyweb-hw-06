--Знайти список студентів у A групі

SELECT s.name AS student_name
FROM students s
JOIN groups gr ON s.group_id = gr.id
WHERE gr.name = 'A';