# Create a program that checks if a given string contains only alphanumeric characters and spaces.

def check_alphanumeric_and_space(text):
    result = None
    for char in text:
        if char.isalnum() or char.isspace():
            result = True
        else:
            result = False
            break
    return result


print(check_alphanumeric_and_space('Hello 123'))
print(check_alphanumeric_and_space('Hello&123'))
