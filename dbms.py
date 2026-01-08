import mysql.connector
from mysql.connector import Error

def create_connection(host, user, password, database=None):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if conn.is_connected():
            print(f"Connected to MySQL{(' db '+database) if database else ''}")
            return conn
    except Error as e:
        print("Connection Error:", e)
    return None


def create_database(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS SchoolDB")
    print("Database ready")
    cursor.close()


def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            grade VARCHAR(10)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Classes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT,
            subject VARCHAR(100),
            score INT,
            FOREIGN KEY (student_id) REFERENCES Students(id) ON DELETE CASCADE
        )
    """)
    conn.commit()
    print("Tables ready")
    cursor.close()


def reset_tables(conn):
    cursor = conn.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("TRUNCATE TABLE Classes")
    cursor.execute("TRUNCATE TABLE Students")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    conn.commit()
    print("Tables cleaned & auto-increment reset")
    cursor.close()


def insert_data(conn):
    cursor = conn.cursor()
    students = [
        ("Alice", 14, "8th"),
        ("Bob", 15, "9th"),
        ("Charlie", 13, "7th"),
        ("David", 14, "8th"),
    ]
    cursor.executemany(
        "INSERT INTO Students (name, age, grade) VALUES (%s, %s, %s)",
        students
    )
    cursor.execute("SELECT id, name FROM Students")
    student_ids = {name: sid for sid, name in cursor.fetchall()}

    classes = [
        (student_ids["Alice"], "Math", 85),
        (student_ids["Alice"], "Science", 90),
        (student_ids["Charlie"], "Math", 78),
        (student_ids["Bob"], "Science", 82),
        (student_ids["David"], "Math", 92),
        (student_ids["Bob"], "Math", 88),
    ]
    cursor.executemany(
        "INSERT INTO Classes (student_id, subject, score) VALUES (%s, %s, %s)",
        classes
    )
    conn.commit()
    print("Sample data inserted safely")
    cursor.close()


def display_data(conn):
    cursor = conn.cursor()
    print("\n--- Students ---")
    cursor.execute("SELECT * FROM Students")
    for row in cursor.fetchall():
        print(row)

    print("\n--- Student Scores (JOIN) ---")
    cursor.execute("""
        SELECT s.name, c.subject, c.score
        FROM Students s
        JOIN Classes c ON s.id = c.student_id
    """)
    for row in cursor.fetchall():
        print(row)
    cursor.close()


def update_and_delete(conn):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Students SET grade = %s WHERE name = %s",
        ("9th", "Alice")
    )
    cursor.execute("""
        DELETE c FROM Classes c
        JOIN Students s ON c.student_id = s.id
        WHERE s.name = %s
    """, ("Charlie",))
    cursor.execute(
        "DELETE FROM Students WHERE name = %s",
        ("Charlie",)
    )
    conn.commit()
    print("Update & delete complete safely")
    cursor.close()


if __name__ == "__main__":
    print("\n===== PYTHON DBMS PROGRAM STARTED =====\n")

    # Step 1: Connect to MySQL server (no database yet)
    server = create_connection("localhost", "root", "Ukalyani@123")
    if server:
        create_database(server)
        server.close()

    # Step 2: Connect again using the SchoolDB database
    db = create_connection("localhost", "root", "Ukalyani@123", "SchoolDB")
    if db:
        create_tables(db)
        reset_tables(db)
        insert_data(db)
        display_data(db)
        update_and_delete(db)
        display_data(db)
        db.close()

    print("\n===== PROGRAM ENDED =====")
