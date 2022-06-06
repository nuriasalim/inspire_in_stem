#assignment
#create employee class, inside it have 2 funtions;employee name and employee salary

class Employee:
    def __init__(self, _name, _salary):
        self.name = _name
        self.salary = _salary

    def details (self):
        print(f'Employee named {self.name} , earns Ksh {self.salary}')
employee1 = Employee('Jane' , str(50000))
employee1.details() 
