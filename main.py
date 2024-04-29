
import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    

# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
sql_1= """
SELECT s.name, ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY AVG(g.grade) DESC
LIMIT 5;
"""
# print("5 студентів із найбільшим середнім балом з усіх предметів: ", execute_query(sql_1))


# Знайти студента із найвищим середнім балом з французського.
sql_2= """
SELECT s.name, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.name = 'French'
GROUP BY s.id
ORDER BY AVG(g.grade) DESC
LIMIT 1;
"""
print("студент із найвищим середнім балом з французського: ", execute_query(sql_2))
print()


# Знайти середній бал у групах з италийського
sql_3= """
SELECT g.subject_id, s.name, gr.name, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
JOIN students s ON g.student_id = s.id
JOIN groups gr ON s.group_id = gr.id
WHERE sub.name = 'Italian'
GROUP BY gr.id;
"""
# print("середній бал у групах з италийського: ", execute_query(sql_3))


# Середній бал потоку
sql_4 = """
SELECT ROUND(AVG(grade), 2) average_grade
FROM grades;
"""
# print("Середній бал потоку: ", execute_query(sql_4))


# --Знайти які курси читає Kathy Fisher
sql_5= """
SELECT DISTINCT t.name AS teacher_name, sub.name AS subject_name
FROM subjects sub
JOIN teachers t ON sub.teacher_id = t.id
WHERE t.name = 'Kathy Fisher';
"""
# --Знайти список студентів у A групі
sql_6 = """
SELECT s.name AS student_name
FROM students s
JOIN groups gr ON s.group_id = gr.id
WHERE gr.name = 'A';
"""


# --Знайти оцінки студентів у B групі з немецького
sql_7 = """
SELECT s.name AS student_name, gr.name, sub.name, g.grade 
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN groups gr ON s.group_id = gr.id
JOIN subjects sub ON g.subject_id = sub.id
WHERE gr.name = 'B' AND sub.name = 'German';
"""


# --Знайти середній бал, який ставить певний викладач зі своїх предметів
sql_8 = """
SELECT t.name AS teacher_name, sub.name AS subjects_name, AVG(g.grade) AS average_grade
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
JOIN teachers t ON sub.teacher_id = t.id
GROUP BY t.id;
"""

# --Знайти список курсів, які відвідує Melissa Mullen
sql_9 = """
--Знайти список курсів, які відвідує Melissa Mullen
SELECT DISTINCT sub.name AS subject_name
FROM subjects sub
JOIN grades g ON sub.id = g.subject_id
JOIN students s ON g.student_id = s.id
WHERE s.name = 'Melissa Mullen';
"""

# --Список курсів, які певному студенту читає певний викладач
sql_10 = """
SELECT DISTINCT sub.name AS subject_name
FROM subjects sub
JOIN grades g ON sub.id = g.subject_id
JOIN students s ON g.student_id = s.id
JOIN teachers t ON sub.teacher_id = t.id
WHERE s.name = 'Monica Knight' AND t.name = 'Philip Collins';
"""


if __name__ == '__main__':

    print('--- Select First ---')
    print(execute_query(sql_1))
    print()

    print('--- Select Second ---')
    print(execute_query(sql_2))
    print()

    print('--- Select Third ---')
    print(execute_query(sql_3))
    print()

    print('--- Select Fourth ---')
    print(execute_query(sql_4))
    print()

    print('--- Select Fifth ---')
    print(execute_query(sql_5))
    print()

    print('--- Select Sixth ---')
    print(execute_query(sql_6))
    print()
    
    print('--- Select Seventh ---')
    print(execute_query(sql_7))
    print()

    print('--- Select Eighth ---')
    print(execute_query(sql_8))
    print()

    print('--- Select Ninth ---')
    print(execute_query(sql_9))
    print()

    print('--- Select Tenth ---')
    print(execute_query(sql_10))
    print()


