USE student_performance;

SELECT COUNT(*) AS Total_Students
FROM students;
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
SELECT ROUND(AVG(Percentage),2) AS Average_Percentage
FROM students;
SELECT Student_Name, Percentage
FROM students
ORDER BY Percentage DESC
LIMIT 1;
SELECT Student_Name, Percentage
FROM students
ORDER BY Percentage ASC
LIMIT 1;
SELECT Department,
ROUND(AVG(Percentage),2) AS Average_Percentage
FROM students
GROUP BY Department;
SELECT Grade,
COUNT(*) AS Total_Students
FROM students
GROUP BY Grade;
SELECT Student_Name,
Attendance
FROM students
WHERE Attendance > 90;
SELECT MAX(Total) AS Highest_Total
FROM students;
SELECT MIN(Total) AS Lowest_Total
FROM students;
SELECT Department,
ROUND(AVG(Percentage),2) AS Average_Percentage
FROM students
GROUP BY Department
HAVING AVG(Percentage) > 80;
SELECT *
FROM students
WHERE Student_Name LIKE 'R%';