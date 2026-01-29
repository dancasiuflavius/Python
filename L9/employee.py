class Employee:
    def __init__(self, name, salary):
        if not name:
            raise ValueError("Eroare: Numele nu poate fi gol!")
        if salary < 0:
            raise ValueError("Eroare: Salariul nu poate fi negativ!")
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        if not department:
            raise ValueError("Eroare: Departamentul nu poate fi gol!")
        self.department = department

    def get_details(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"


try:
    emp = Employee("John", 3000)
    print(emp.get_details())

    mgr = Manager("Alice", 5000, "IT")
    print(mgr.get_details())

except ValueError as e:
    print(e)
