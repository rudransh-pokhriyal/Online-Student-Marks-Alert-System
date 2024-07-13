import sqlite3


conn = sqlite3.connect('school.db')


cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        ''')
cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            parent_contact TEXT NOT NULL
        )
        ''')
cursor.execute('''
        CREATE TABLE IF NOT EXISTS marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            subject TEXT NOT NULL,
            mark INTEGER NOT NULL,
            FOREIGN KEY(student_id) REFERENCES students(student_id)
        )
        ''')


students_data = [
    (1, 'Smith Doe', '+919475603678'),
    (2, 'Joe Black', '+1234567891'),
    (3, 'Emily Johnson', '+1234567892'),
    (4, 'Michael Stark', '+1234567893')
]

cursor.executemany('''
INSERT INTO students (student_id, name, parent_contact)
VALUES (?, ?, ?)
''', students_data)


marks_data = [
    (1, 'Math', 75),
    (1, 'English', 45),
    (2, 'Math', 85),
    (2, 'English', 55),
    (3, 'Math', 56),
    (3, 'English', 65),
    (4, 'Math', 90),
    (4, 'English', 70)
]

cursor.executemany('''
INSERT INTO marks (student_id, subject, mark)
VALUES (?, ?, ?)
''', marks_data)

conn.commit()
conn.close()

print("Database initialized and sample data inserted successfully.")
