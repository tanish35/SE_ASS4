import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME1"),
    ssl_ca="ca.pem",
)
cursor = conn.cursor()

cursor.execute("SHOW DATABASES")
databases = [db[0] for db in cursor.fetchall()]

if "defaultdb" in databases:
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
        CREATE TABLE teachers (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100),
            subject_id INT,
            FOREIGN KEY (subject_id) REFERENCES subjects(id)
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
