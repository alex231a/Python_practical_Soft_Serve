# Define a class Employee.
# In the class Employee implement the instance attributes as firstname, lastname and salary.
# Create the static method from_string() which parses a string containing these attributes
# and assigns them to the correct properties.
# Properties will be separated by a dash.

# Examples:
# emp1 = Employee("Mary", "Sue", 60000)
# emp2 = Employee.from_string("John-Smith-55000")
# emp1.firstname ➞ "Mary"
# emp1.salary ➞ 60000
# emp2.firstname ➞ "John"


class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = int(salary)


    @staticmethod
    def from_string(some_str):
        p_list = some_str.split('-')
        if len(p_list) == 3:
            first_name, last_name, salary_e = p_list
            return Employee(first_name, last_name, salary_e)
        else:
            raise ValueError('Invalid string')




emp1 = Employee("Mary", "Sue", 60000)
print(emp1.firstname)
print(emp1.salary)

emp2 = Employee.from_string("John-Smith-55000")
print(emp2.firstname)
print(emp2.salary)