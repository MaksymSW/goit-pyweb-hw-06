--Таблиця студентів
--DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    group_id INTEGER NOT NULL,
    FOREIGN KEY (group_id) REFERENCES groups(id)
);

-- Таблиця груп
CREATE TABLE groups (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- Таблиця викладачів
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- Таблиця предметів, із вказівкою викладача, який читає предмет
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    teacher_id VARCHAR(50) NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

-- Таблиця де у кожного студента є оцінки з предметів із зазначенням коли оцінку отримано
CREATE TABLE grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    date TEXT,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);
