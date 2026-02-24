class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def display_details(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, first_name, last_name, age, employee_id, salary):
        super().__init__(first_name, last_name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_details(self):
        self.display_details()
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ₹{self.salary:,.2f}")


class Manager(Employee):
    def __init__(self, first_name, last_name, age, employee_id, salary, department, team_size):
        super().__init__(first_name, last_name, age, employee_id, salary)
        self.department = department
        self.team_size = min(team_size, 10)  

    def display_manager_details(self):
        self.display_employee_details()
        print("Manager Details:")
        print(f"Department: {self.department}")
        print(f"Team Size: {self.team_size} people")


# Example usage
if __name__ == "__main__":
    mgr = Manager("Steve", "Harrington", 25, "EMP101", 10,000, "IT", 15)
    mgr.display_manager_details()