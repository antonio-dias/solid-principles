# Reasons to change
# 1. Changes in Employee Attributes
# 2. Changes in Database
# 3. Changes in Tax Calculation

class Employee:

    def __init__(self):
        self.employeeId = ""
        self.employeeName = ""
        self.employeeType = ""

    def save(self):
        connection = None
        try:
            connection = ("jdbc:mysql://localhost:3306/MyDB", "root", "password")
        except:
            print("Error")

    def calculateTax(self):
        if self.employeeType == "fulltime":
            # Tax calc for full time employee
            pass
        elif self.employeeType == "contract":
            # Tax calc for contractors
            pass

    def setEmployeeId(self, employeeID):
        self.employeeId = employeeID

    def setEmployeeName(self, employeeName):
        self.employeeName = employeeName

    def setEmployeeType(self, employeeType):
        self.employeeType = employeeType
