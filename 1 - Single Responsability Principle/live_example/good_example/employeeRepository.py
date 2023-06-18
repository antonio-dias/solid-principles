class EmployeeRepository:

    def save(self, employee):
        obj = employee
        connection = None
        try:
            connection = ("jdbc:mysql://localhost:3306/MyDB", "root", "password")
        except:
            print("Error")