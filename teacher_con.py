import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME"),
    ssl_ca="ca.pem",
)
cursor = conn.cursor()

def get_teacher_id(name):
    cursor.execute("SELECT id, subject_id FROM teachers WHERE name = %s", (name,))
    return cursor.fetchone() 

def get_students_and_marks(subject_id):
    query = """
        SELECT students.id, students.name, students.roll_number, marks.marks
        FROM students
        JOIN marks ON students.id = marks.student_id
        WHERE marks.subject_id = %s
    """
    cursor.execute(query, (subject_id,))
    return cursor.fetchall()

def update_marks(subject_id):
    students = get_students_and_marks(subject_id)
    
    if not students:
        print("No students found for your subject.")
        return
    
    print("\nYour Students and Marks:")
    print("ID | Name | Roll Number | Marks")
    for student in students:
        print(f"{student[0]} | {student[1]} | {student[2]} | {student[3]}")

    while True:
        student_id = input("\nEnter Student ID to update marks (or 'submit' to finish): ").strip()

        if student_id.lower() == "submit":
            conn.commit()
            print("Marks updated successfully!")
            break
        
        try:
            student_id = int(student_id)
            new_marks = int(input("Enter new marks: ").strip())

            cursor.execute("""
                UPDATE marks 
                SET marks = %s 
                WHERE student_id = %s AND subject_id = %s
            """, (new_marks, student_id, subject_id))

            print("Marks updated! Enter another ID or type 'submit' to finish.")
        except ValueError:
            print("Invalid input. Please enter a valid Student ID and Marks.")

def teacher_login():
    teacher_name = input("Enter your name: ").strip()
    teacher_data = get_teacher_id(teacher_name)

    if not teacher_data:
        print("Teacher not found! Please enter a valid name.")
        return

    teacher_id, subject_id = teacher_data
    print(f"\nWelcome, {teacher_name}! You can edit marks for your subject.\n")
    update_marks(subject_id)


teacher_login()
cursor.close()
conn.close()
