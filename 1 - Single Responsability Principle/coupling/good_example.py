class StudentRepository:

    def save(self):
        connection = None
        stmt = None
        try:
            connection = ("jdbc:mysql://localhost:3306/MyDB", "root", "password")
        except:
            print("Error")

class Student:

    def __init__(self):
        self.studentId = ""
        self.studentDOB = ""
        self.address = ""

    def save(self):
        StudentRepository.save()

    def getStudentId(self):
        return self.studentId

    def setStudentId(self, studentId):
        self.studentId = studentId

