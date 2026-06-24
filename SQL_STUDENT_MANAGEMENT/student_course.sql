USE school;

CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    course_id INT
);

CREATE TABLE Course (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    duration_months INT
);

SHOW TABLES;

INSERT INTO Course VALUES (101, 'Python', 3);
INSERT INTO Course VALUES (102, 'Java', 4);
INSERT INTO Course VALUES (103, 'SQL', 2);

INSERT INTO Student VALUES (1, 'Rahul', 20, 101);
INSERT INTO Student VALUES (2, 'Anjali', 21, 102);
INSERT INTO Student VALUES (3, 'Arjun', 19, 103);
INSERT INTO Student VALUES (4, 'Meera', 22, 101);

SELECT * FROM Student;

SELECT * FROM Course;

SELECT * FROM Student
WHERE age > 20;

SELECT * FROM Student
WHERE course_id = 101;

UPDATE Student
SET age = 23
WHERE student_id = 4;

UPDATE Course
SET duration_months = 5
WHERE course_id = 102;

DELETE FROM Student
WHERE student_id = 3;

INSERT INTO Student VALUES (5, 'Akhil', 20, 103);

SELECT Student.name, Course.course_name
FROM Student
JOIN Course
ON Student.course_id = Course.course_id;

SELECT Student.student_id,
       Student.name,
       Student.age,
       Course.course_name
FROM Student
JOIN Course
ON Student.course_id = Course.course_id;

SELECT COUNT(*) AS Total_Students
FROM Student;

