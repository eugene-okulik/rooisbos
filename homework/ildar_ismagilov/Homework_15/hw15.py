import mysql.connector as mysql

# creating connection
db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
# creating cursor
cursor = db.cursor(dictionary=True, buffered=True)

# creating student
query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
values = ('Forrest', 'Gump')
cursor.execute(query, values)
student_id = cursor.lastrowid
cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
fetch_result = cursor.fetchone()
print(fetch_result)
db.commit()

# creating books
query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = [
    ('Alice in Wonderland', student_id),
    ('Hamlet', student_id)
]
cursor.executemany(query, values)
cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
print(cursor.fetchall())
db.commit()

# creating group
query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values = ('The A-Team', '01/19/2025', '01/19/2026')
cursor.execute(query, values)
group_id = cursor.lastrowid
cursor.execute("SELECT * FROM `groups` WHERE id = %s", (group_id,))
print(cursor.fetchone())
db.commit()

# updating student's group
query = "UPDATE students SET group_id = %s WHERE id = %s"
values = (group_id, student_id)
cursor.execute(query, values)
cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
print(cursor.fetchone())
db.commit()

# creating variables for lessons
lesson1, lesson2, lesson3, lesson4 = 'German_reading', 'German_writing', 'Spanish_reading', 'Spanish_writing'

# creating first subject
query = "INSERT INTO subjets (title) VALUES (%s)"
values = ('German 101',)
cursor.execute(query, values)
subject_id = cursor.lastrowid
cursor.execute("SELECT * FROM subjets WHERE id = %s", (subject_id,))
print(cursor.fetchone())
db.commit()

# creating first lesson
query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values = (lesson1, subject_id)
cursor.execute(query, values)
lesson1_id = cursor.lastrowid
cursor.execute("SELECT * FROM lessons WHERE subject_id = %s", (subject_id,))
print(cursor.fetchone())
db.commit()

# creating second lesson
query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values = (lesson2, subject_id)
cursor.execute(query, values)
lesson2_id = cursor.lastrowid
cursor.execute("SELECT * FROM lessons WHERE subject_id = %s", (subject_id,))
print(cursor.fetchone())
db.commit()

# creating second subject
query = "INSERT INTO subjets (title) VALUES (%s)"
values = ('Spanish 101',)
cursor.execute(query, values)
subject_id = cursor.lastrowid
cursor.execute("SELECT * FROM subjets WHERE id = %s", (subject_id,))
print(cursor.fetchone())
db.commit()

# creating 2 lessons
query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values = [
    (lesson3, subject_id),
    (lesson4, subject_id)
]
cursor.executemany(query, values)
cursor.execute("SELECT * FROM lessons WHERE subject_id = %s", (subject_id,))
print(cursor.fetchall())
db.commit()

# getting lessons_id
cursor.execute("SELECT id FROM lessons WHERE title = %s", (lesson1,))
german_reading_id = cursor.fetchone()['id']
cursor.execute("SELECT id FROM lessons WHERE title = %s", (lesson2,))
german_writing_id = cursor.fetchone()['id']
cursor.execute("SELECT id FROM lessons WHERE title = %s", (lesson3,))
spanish_reading_id = cursor.fetchone()['id']
cursor.execute("SELECT id FROM lessons WHERE title = %s", (lesson4,))
spanish_writing_id = cursor.fetchone()['id']

# creating marks
query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values = [
    ('A', german_reading_id, student_id),
    ('A+', german_writing_id, student_id),
    ('A-', spanish_reading_id, student_id),
    ('B', spanish_writing_id, student_id)
]
cursor.executemany(query, values)
cursor.execute("SELECT * FROM marks WHERE student_id = %s", (student_id,))
print(cursor.fetchall())
db.commit()

# selecting all student books
cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
print(cursor.fetchall())

# JOIN request
query = '''
SELECT students.name,
       students.second_name,
       books.title   AS book,
       groups.title  AS `group`,
       subjets.title AS subject,
       lessons.title AS lesson,
       marks.value   AS mark
FROM   students
JOIN   books
ON     students.id = books.taken_by_student_id
JOIN   `groups`
ON     students.group_id = groups.id
JOIN   marks
ON     students.id = marks.student_id
JOIN   lessons
ON     marks.lesson_id = lessons.id
JOIN   subjets
ON     lessons.subject_id = subjets.id
WHERE  name = %s
AND second_name = %s 
'''
cursor.execute(query, (fetch_result['name'], fetch_result['second_name']))
print(cursor.fetchall())

# closing connection
db.close()
