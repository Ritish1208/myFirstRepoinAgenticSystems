DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    score INTEGER,
    passed BOOLEAN,
    class INTEGER
);


INSERT INTO students (id, name, score, passed, class) VALUES
(1, 'Aarav', 92, 1, 10),
(2, 'Diya', 76, 1, 10),
(3, 'Rohan', 65, 0, 9),
(4, 'Meera', 88, 1, 10),
(5, 'Kabir', 54, 0, 9),
(6, 'Ananya', 95, 1, 10),
(7, 'Rahul', 81, 1, 9),
(8, 'Sneha', 73, 1, 9),
(9, 'Arjun', 84, 1, 10),
(10, 'Kavya', 69, 0, 9);

SELECT * FROM students;

SELECT name, score FROM students;

SELECT * FROM students
Where score>80;

SELECT * FROM students
where score > 80 and passed= true;

SELECT * FROM students
where score >85 or class = 9;

SELECT * FROM students
Where  NOT passed = 1;

SELECT  DISTINCT class FROM students;

SELECT*FROM students
ORDER BY score DESC
LIMIT 5;

SELECT * FROM students
ORDER BY class ASC, score DESC;

SELECT name, score as final_score From students;

SELECT name, score 
FROM students
WHERE  score>75
ORDER BY score DESC
LIMIT 3;
