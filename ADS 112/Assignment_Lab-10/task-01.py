# Write a Python class called 'Student' that calculates the GPA based on a list of grades.

class Student:
    def __init__(self, name: str, grade: list[float]):
        self.name = name
        self.grade = grade

    def result(self) -> float:
        print("Student Name:", self.name)
        print("Result:", end=" ")
        if not self.grade:
            return 0.00
        return sum(self.grade) / len(self.grade)


rt = Student("RT", [4,3.5,4,4,4,3.75, 4])
print(rt.result())

jeion = Student("Jeion", [3.5,2,3.5,2,4])
print(jeion.result())