import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database="marks_db"
)
cursor = conn.cursor()
subjects = [("Race Strategy",), ("Car Aerodynamics",), ("Track Analysis",)]
cursor.executemany("INSERT INTO subjects (name) VALUES (%s)", subjects)

cursor.execute("SELECT id, name FROM subjects")
subject_map = {name: id for id, name in cursor.fetchall()}
teachers = [
    ("Toto Wolff", subject_map["Race Strategy"]),
    ("Christian Horner", subject_map["Car Aerodynamics"]),
    ("Fred Vasseur", subject_map["Track Analysis"])
]
cursor.executemany("INSERT INTO teachers (name, subject_id) VALUES (%s, %s)", teachers)
cursor.execute("SELECT id, name FROM teachers")
teacher_map = {name: id for id, name in cursor.fetchall()}

students = [
    ("Max Verstappen", "S001"),
    ("Lewis Hamilton", "S002"),
    ("Charles Leclerc", "S003"),
    ("Lando Norris", "S004"),
    ("Fernando Alonso", "S005"),
    ("George Russell", "S006"),
    ("Carlos Sainz", "S007"),
    ("Sergio Perez", "S008"),
    ("Oscar Piastri", "S009"),
    ("Pierre Gasly", "S010")
]
cursor.executemany("INSERT INTO students (name, roll_number) VALUES (%s, %s)", students)
cursor.execute("SELECT id, roll_number FROM students")
student_map = {roll: id for id, roll in cursor.fetchall()}

marks = [
    (student_map["S001"], subject_map["Race Strategy"], 95),
    (student_map["S001"], subject_map["Car Aerodynamics"], 88),
    (student_map["S001"], subject_map["Track Analysis"], 92),
    
    (student_map["S002"], subject_map["Race Strategy"], 89),
    (student_map["S002"], subject_map["Car Aerodynamics"], 94),
    (student_map["S002"], subject_map["Track Analysis"], 90),
    
    (student_map["S003"], subject_map["Race Strategy"], 87),
    (student_map["S003"], subject_map["Car Aerodynamics"], 85),
    (student_map["S003"], subject_map["Track Analysis"], 93),
    
    (student_map["S004"], subject_map["Race Strategy"], 91),
    (student_map["S004"], subject_map["Car Aerodynamics"], 89),
    (student_map["S004"], subject_map["Track Analysis"], 88),
    
    (student_map["S005"], subject_map["Race Strategy"], 96),
    (student_map["S005"], subject_map["Car Aerodynamics"], 92),
    (student_map["S005"], subject_map["Track Analysis"], 90),
    
    (student_map["S006"], subject_map["Race Strategy"], 85),
    (student_map["S006"], subject_map["Car Aerodynamics"], 87),
    (student_map["S006"], subject_map["Track Analysis"], 82),
    
    (student_map["S007"], subject_map["Race Strategy"], 88),
    (student_map["S007"], subject_map["Car Aerodynamics"], 86),
    (student_map["S007"], subject_map["Track Analysis"], 91),
    
    (student_map["S008"], subject_map["Race Strategy"], 90),
    (student_map["S008"], subject_map["Car Aerodynamics"], 92),
    (student_map["S008"], subject_map["Track Analysis"], 85),
    
    (student_map["S009"], subject_map["Race Strategy"], 83),
    (student_map["S009"], subject_map["Car Aerodynamics"], 80),
    (student_map["S009"], subject_map["Track Analysis"], 87),
    
    (student_map["S010"], subject_map["Race Strategy"], 86),
    (student_map["S010"], subject_map["Car Aerodynamics"], 89),
    (student_map["S010"], subject_map["Track Analysis"], 84)
]
cursor.executemany("INSERT INTO marks (student_id, subject_id, marks) VALUES (%s, %s, %s)", marks)

conn.commit()
print("Database seeded successfully with F1-themed data! 🏎️🔥")

cursor.close()
conn.close()
