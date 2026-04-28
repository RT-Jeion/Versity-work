 # Write a class 'GeometricShape' with methods to calculate areas.

class GeometricShape:
	def area_circle(self, radius: float) -> float:
		return 3.1416 * radius * radius

	def area_square(self, side: float) -> float:
		return side * side

	def area_rectangular(self, height: float, width: float) -> float:
		return height * width


shape = GeometricShape()

print("Area of Circle:", shape.area_circle(3))
print("Area of Square:", shape.area_square(5))
print("Area of Rectangular:", shape.area_rectangular(2,4))