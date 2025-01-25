import dotenv
import csv
import os
import mysql.connector as mysql

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

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
AND `groups`.title = %s
AND books.title = %s
AND subjets.title = %s
AND lessons.title = %s
AND marks.value = %s
'''

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
csv_file_path = os.path.join(homework_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv")

with open(csv_file_path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    for row in file_data:
        cursor.execute(query, tuple(row))
        if cursor.fetchone() is None:
            print(row)
