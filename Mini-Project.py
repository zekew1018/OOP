import mysql.connector
db = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="MasterDB"
)
cursor = db.cursor()
cursor.execute("T")
print("T")
db.close()

class Student_Master(object):
    def __init__(self):
        self.stu_id = "123456789"
        self.stu_name = "Blank"
        self.stu_major = "GD"
        self.stu_courses = "OOP"
        self.stu_cgpa = "4"

class Faculty_Master(object):
    def __init__(self):
        self.fac_id = "123456789"
        self.fac_name = "Blank"
        self.fac_department = "GD"
        self.fac_courses = "OOP"
