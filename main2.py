class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary
        print(f"Employee object for {self.name} created.")
        print("Employee Details:")
        print(f"Name: {self.name}")
        print(f"ID: {self.emp_id}")
        print(f"Department: {self.department}")
        print(f"Salary: { self.salary}")
    def __del__(self):
        print(f"Employee object for {self.name} deleted.")
def created_and_deleate_employment():
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    department = input("Enter department: ")
    salary = input("Enter salary: ")
    emp = Employee(name, emp_id, department, salary)
    del emp
created_and_deleate_employment()