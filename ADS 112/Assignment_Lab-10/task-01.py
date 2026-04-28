# Write a Python class called 'Student' that calculates the GPA based on a list of grades.

class Student:
	def __init__(self, name, grades):
		self.name = name
		self.grades = grades

	def calculate_gpa(self):
		if not self.grades:
			return 0.0
		return sum(self.grades) / len(self.grades)


if __name__ == "__main__":
	student = Student("Asha", [3.7, 3.3, 3.9, 3.5])
	print(f"{student.name}'s GPA: {student.calculate_gpa():.2f}")