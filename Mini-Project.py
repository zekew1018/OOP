import mysql.connector
db = mysql.connector.connect(
    host = "localhost"
    user = "root"         
    password = "password" 
		database = "MasterDB"
)
cursor = db.cursor()
class Student_Master:
    def __init__(self, stu_name, stu_major, stu_courses, stu_cgpa):
        self.stu_name = stu_name
        self.stu_major = stu_major
        self.stu_courses = stu_courses
        self.stu_cgpa = stu_cgpa

class Faculty_Master:
    def __init__(self, fac_id, fac_name, fac_department, fac_teaches_courses):
        self.fac_id = fac_id
        self.fac_name = fac_name
        self.fac_department = fac_department
        self.fac_teaches_courses = fac_teaches_courses

def build_objects():
    students = [
        Student_Master(1001, "Zeke Wiggins", "Game Design",
                       ["CS101", "MATH201", "PHY101"], 3.85),
        Student_Master(1002, "Elijah Powell", "Mathematics",
                       ["MATH201", "MATH301", "STAT210"], 3.40),
        Student_Master(1003, "Keene Elkins", "Biology",
                       ["BIO110", "CHEM101", "STAT210"], 3.72),
        Student_Master(1004, "Colton Tapp", "Music",
                       ["MUS101", "MUS220", "ENG102"], 3.15),
        Student_Master(1005, "Wyatt Olinger", "Computer Science",
                       ["CS101", "CS210", "ENG102"], 3.95),
    ]
    faculty = [
        Faculty_Master(2001, "Dr. Justus", "Computer Science",
                       ["CS101", "CS210"]),
        Faculty_Master(2002, "Dr. Wilkeson", "Mathematics",
                       ["MATH201", "MATH301", "STAT210"]),
        Faculty_Master(2003, "Dr. Ellenbarger", "Biology",
                       ["BIO110", "CHEM101"]),
        Faculty_Master(2004, "Prof. ", "Music",
                       ["MUS101", "MUS220"]),
        Faculty_Master(2005, "Dr. Rhodes", "English",
                       ["ENG102"]),
    ]
    return students, faculty


def get_connection():
    """Connect to the school_db database, creating it if needed."""
    server = mysql.connector.connect(**MasterDB)
    cursor = server.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    cursor.close()
    server.database = database
    return server


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS Student_Master")
    cursor.execute("DROP TABLE IF EXISTS Faculty_Master")
    cursor.execute("""
        CREATE TABLE Student_Master (
            stu_id      INT PRIMARY KEY,
            stu_name    VARCHAR(100) NOT NULL,
            stu_major   VARCHAR(100),
            stu_courses VARCHAR(255),
            stu_cgpa    DECIMAL(3,2)
        )""")
    cursor.execute("""
        CREATE TABLE Faculty_Master (
            fac_id              INT PRIMARY KEY,
            fac_name            VARCHAR(100) NOT NULL,
            fac_department      VARCHAR(100),
            fac_teaches_courses VARCHAR(255)
        )""")
    conn.commit()
    cursor.close()
    conn.close()
    print("Tables Student_Master and Faculty_Master created.")


def write_objects(students, faculty):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executemany(
        "REPLACE INTO Student_Master "
        "(stu_id, stu_name, stu_major, stu_courses, stu_cgpa) "
        "VALUES (%s, %s, %s, %s, %s)",
        [(s.stu_id, s.stu_name, s.stu_major,
          ",".join(s.stu_courses), s.stu_cgpa) for s in students])
    cursor.executemany(
        "REPLACE INTO Faculty_Master "
        "(fac_id, fac_name, fac_department, fac_teaches_courses) "
        "VALUES (%s, %s, %s, %s)",
        [(f.fac_id, f.fac_name, f.fac_department,
          ",".join(f.fac_teaches_courses)) for f in faculty])
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Wrote {len(students)} students and {len(faculty)} faculty to the database.")


def read_and_display():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student_Master")
    stu_rows = cursor.fetchall()
    cursor.execute("SELECT * FROM Faculty_Master")
    fac_rows = cursor.fetchall()
    cursor.close()
    conn.close()

    students = [Student_Master(r[0], r[1], r[2], r[3].split(","), float(r[4]))
                for r in stu_rows]
    faculty = [Faculty_Master(r[0], r[1], r[2], r[3].split(","))
               for r in fac_rows]

    print("\n" + "=" * 60)
    print("STUDENTS (read from database)")
    print("=" * 60)
    for s in students:
        print(s)
    print("\n" + "=" * 60)
    print("FACULTY (read from database)")
    print("=" * 60)
    for f in faculty:
        print(f)
    print()

def main():
    students, faculty = build_objects()
    menu = """
School Database Menu:
1. Create database table
2. Add student and faculty database
3. Read back and display all details
4. Run all steps (1, 2, 3)
5. Exit
Choice: """
    while True:
        choice = input(menu).strip()
        try:
            if choice == "1":
                create_tables()
            elif choice == "2":
                write_objects(students, faculty)
            elif choice == "3":
                read_and_display()
            elif choice == "4":
                create_tables()
                write_objects(students, faculty)
                read_and_display()
            elif choice == "5":
                print("Thanks for using MasterDB!")
                break
            else:
                print("Invalid choice.")
if __name__ == "__main__":
	main()
