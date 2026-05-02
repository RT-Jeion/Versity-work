class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def get_role(self):
        pass


class Student(Person):
    def __init__(self, name, email, department):
        super().__init__(name, email)
        self.role = "Current Student"
        self.department = department
        self.__marks = 0

    def get_role(self):
        return "Current Student"

    def get_marks(self):
        return self.__marks
    
    def set_marks(self, marks):
        self.marks = marks

class GraduateStudent(Student):
    def get_role(self):
        return "Graduate Student"
    
    def grade(self, marks):
        set_marks(marks)



data = [
"Rakib|rakib@gmail.com|85,90,78|CSE",
"Sadia|sadia@gmail.com|88,92,95|CSE",
"Nayeem|nayeem@gmail.com|70,60,75|EEE",
"Rakib|rakib@gmail.com|85,90,78|CSE" # duplicate
]

data = list(set(data))

def parse_data(d):
    data_list = d.split("|")
    name = data_list[0]
    email = data_list[1]
    marks = data_list[2].split(",")
    department = data_list[3]
    return name, email, marks, department
print(data)
data1 = parse_data(data[0])
rt = GraduateStudent(data1[0], data1[1], data1[3])

print(rt.get_role())
print(rt.name)
rt.set_marks(data1[2])
print(rt.marks)
