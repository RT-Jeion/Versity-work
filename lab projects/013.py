from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @abstractmethod
    def get_role(self):
        pass


class Student(Person):
    def __init__(self, name, email, marks, department):
        super().__init__(name, email)
        self.__marks = marks
        self.department = department

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    def get_role(self):
        return "Student"

    def get_average(self):
        avg = lambda marks: sum(marks) / len(marks)
        return avg(self.__marks)

    def get_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        else:
            return "F"


class GraduateStudent(Student):
    def get_role(self):
        return "Graduate Student"

    def get_grade(self):
        avg = self.get_average()
        if avg >= 92:
            return "A"
        elif avg >= 82:
            return "B"
        elif avg >= 72:
            return "C"
        else:
            return "F"


data = [
    "Rakib|rakib@gmail.com|85,90,78|CSE",
    "Sadia|sadia@gmail.com|88,92,95|CSE",
    "Nayeem|nayeem@gmail.com|70,60,75|EEE",
    "Rakib|rakib@gmail.com|85,90,78|CSE"
]

unique_data = list(set(data))

students_dict = {}

for record in unique_data:
    name, email, marks_str, dept = record.split("|")
    marks = list(map(int, marks_str.split(",")))
    student = Student(name, email, marks, dept)
    students_dict[email] = student

departments = set()
dept_count = {}

top_student = None
highest_avg = 0

for student in students_dict.values():
    avg = student.get_average()

    departments.add(student.department)
    dept_count[student.department] = dept_count.get(student.department, 0) + 1

    if avg > highest_avg:
        highest_avg = avg
        top_student = student

print("=== All Students with Grades ===")
for student in students_dict.values():
    print(f"Name: {student.name}, Email: {student.email}, "
          f"Dept: {student.department}, Avg: {student.get_average():.2f}, "
          f"Grade: {student.get_grade()}")

print("\n=== Department-wise Student Count ===")
for dept, count in dept_count.items():
    print(f"{dept}: {count}")

print("\n=== Top Student ===")
print(f"Name: {top_student.name}, Email: {top_student.email}, "
      f"Avg: {top_student.get_average():.2f}, Grade: {top_student.get_grade()}")
