INSERT INTO students (name, second_name, group_id) VALUES ('Corben', 'Dallas', 142)

INSERT INTO books (title, taken_by_student_id) VALUES ('The Holy Bible', 311)
INSERT INTO books (title, taken_by_student_id) VALUES ('Crime and punishment', 311)

INSERT INTO `groups` (title, start_date, end_date) VALUES ('Modern talking', '01/15/2025', '01/15/2026')

INSERT INTO subjets (title) VALUES ('Python 101')
INSERT INTO subjets (title) VALUES ('SQL 101')

INSERT INTO lessons (title, subject_id) VALUES ('Python_basics', 280)
INSERT INTO lessons (title, subject_id) VALUES ('Git_basics', 280)
INSERT INTO lessons (title, subject_id) VALUES ('Creating DB', 281)
INSERT INTO lessons (title, subject_id) VALUES ('Maintaining DB', 281)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('A', 637, 311)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('B', 638, 311)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('B+', 639, 311)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('A-', 640, 311)

SELECT * FROM marks WHERE student_id = 311
SELECT * FROM books WHERE taken_by_student_id = 311

SELECT students.name,
       students.second_name,
       books.title   AS book,
       groups.title  AS `group`,
       subjets.title AS subject,
       lessons.title AS lesson,
       marks.value   AS mark
FROM   students
       JOIN books
         ON students.id = books.taken_by_student_id
       JOIN `groups`
         ON students.group_id = groups.id
       JOIN marks
         ON students.id = marks.student_id
       JOIN lessons
         ON marks.lesson_id = lessons.id