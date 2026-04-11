# Implement a program that validates a U.S. phone number (e.g., (123) 456-7890) using regex.

import re

def validating_number(number):
    pattern = r'\([0-9]{3}\) [0-9]{3}-[0-9]{4}'
    return bool(re.match(pattern, number))

print(validating_number("(123) 456-7890"))
print(validating_number("123-789-2030"))
