--Список курсів, які певному студенту читає певний викладач

SELECT DISTINCT sub.name AS subject_name
FROM subjects sub
JOIN grades g ON sub.id = g.subject_id
JOIN students s ON g.student_id = s.id
JOIN teachers t ON sub.teacher_id = t.id
WHERE s.name = 'Monica Knight' AND t.name = 'Philip Collins';
