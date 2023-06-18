from employeeRepository import EmployeeRepository
from taxCalculator import TaxCalculator

class Employee:

    def __init__(self):
        self.employeeId = ""
        self.employeeName = ""
        self.employeeType = ""

    def save(self):
        obj = {self.employeeId, self.employeeName, self.employeeType}
        EmployeeRepository.save(obj)

    def calculateTax(self):
        TaxCalculator.calculateTax(self.employeeType)

    def setEmployeeId(self, employeeID):
        self.employeeId = employeeID

    def setEmployeeName(self, employeeName):
        self.employeeName = employeeName

    def setEmployeeType(self, employeeType):
        self.employeeType = employeeType
