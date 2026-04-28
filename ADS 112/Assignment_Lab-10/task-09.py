# Write a Python class 'Temperature' to convert between Celsius and Fahrenheit.

class Temperature:
    def cel_to_fahr(self, celsius: float):
        print(f"{celsius} Celsius to Fahrenheit", end=" ")
        return (celsius * 9/5 ) + 32

    def fahr_to_cel(self, fahrenheit: float):
        print(f"{fahrenheit} Fahrenheit to Celsius", end=" ")
        return (fahrenheit - 32 ) * 5/9

temperature = Temperature()

print(temperature.fahr_to_cel(20))
print(temperature.cel_to_fahr(20))

