class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def work(self):
        return f"{self.name} is working with employee ID {self.employee_id}."
        

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying with student ID {self.student_id}."
    


emp = Employee("Alice", 30, "E123")
student = Student("Bob", 20, "S456")
print(emp.greet())
print(emp.work())
print(student.greet())
print(student.study())
