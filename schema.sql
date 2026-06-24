CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL
);

CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';

CREATE INDEX idx_student_name
ON students(name);

CREATE INDEX idx_course_name
ON courses(course_name);

INSERT INTO students(name,email)
VALUES
('Anu','anu@gmail.com'),
('Rahul','rahul@gmail.com');

INSERT INTO courses(course_name)
VALUES
('Python'),
('PostgreSQL');

INSERT INTO enrollments(student_id,course_id)
VALUES
(1,1),
(1,2),
(2,1);

SELECT * FROM students;

SELECT * FROM courses;

SELECT * FROM enrollments;

SELECT
s.name,
c.course_name
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
JOIN courses c
ON e.course_id = c.course_id;