import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306
)
cursor = conn.cursor()

cursor.execute("SHOW DATABASES")
databases = [db[0] for db in cursor.fetchall()]

if "marks_db" not in databases:
    print("Creating database and tables...")
    cursor.execute("CREATE DATABASE marks_db")
    conn.database = "marks_db"
    cursor.execute("""
        CREATE TABLE students (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100),
            roll_number VARCHAR(20) UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE subjects (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100)
        )
    """)

    cursor.execute("""
        CREATE TABLE marks (
            id INT PRIMARY KEY AUTO_INCREMENT,
            student_id INT,
            subject_id INT,
            marks INT,
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (subject_id) REFERENCES subjects(id)
        )
    """)

    print("Database and tables created successfully!")
else:
    print("Database already exists. No changes made.")

cursor.close()
conn.close()
