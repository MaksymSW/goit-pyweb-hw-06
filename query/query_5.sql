--Знайти які курси читає Kathy Fisher

SELECT DISTINCT t.name AS teacher_name, sub.name AS subject_name
FROM subjects sub
JOIN teachers t ON sub.teacher_id = t.id
WHERE t.name = 'Kathy Fisher';