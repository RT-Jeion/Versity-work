# Write a Python class 'Employee' with id, name, department, and display method.

class Employee:
    def __init__(self, name, id,department):
        self.name = name
        self.id = id
        self.department = department

    def display(self):
        print("---Employee Info---")
        print("Name:", self.name)
        print("ID:", self.id)
        print("Department:", self.department)
        print()

rt = Employee("RT Jeion", "007", "Backend")
rejuwan = Employee("Rejuwan Tasfic", "001", "DevOps")

rt.display()
rejuwan.display()