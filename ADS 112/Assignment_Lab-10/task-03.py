# Write a class 'GeometricShape' with methods to calculate areas.


class GeometricShape:
	def area_circle(self, radius):
		return 3.141592653589793 * radius * radius

	def area_rectangle(self, length, width):
		return length * width

	def area_square(self, side):
		return side * side


if __name__ == "__main__":
	shape = GeometricShape()
	print(f"Circle area (r=4): {shape.area_circle(4):.2f}")
	print(f"Rectangle area (6x3): {shape.area_rectangle(6, 3):.2f}")
	print(f"Square area (5): {shape.area_square(5):.2f}")

