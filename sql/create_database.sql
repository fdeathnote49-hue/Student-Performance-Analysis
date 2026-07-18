CREATE DATABASE student_performance;

USE student_performance;
SELECT *
FROM students;
SELECT Student_Name, Percentage
FROM students
ORDER BY Percentage DESC
LIMIT 5;
SELECT Student_Name, Percentage
FROM students
ORDER BY Percentage ASC
LIMIT 5;


CREATE TABLE students (
    Student_ID VARCHAR(10) PRIMARY KEY,
    Student_Name VARCHAR(50),
    Gender VARCHAR(10),
    Age INT,
    Department VARCHAR(20),
    Semester INT,
    Attendance INT,
    Math INT,
    Science INT,
    English INT,
    Computer INT,
    Total INT,
    Percentage DECIMAL(5,2),
    Grade VARCHAR(5)
);