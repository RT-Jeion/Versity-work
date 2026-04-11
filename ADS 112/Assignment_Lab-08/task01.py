# Implement a function that checks if a string is a valid email address using regular expressions
import re

def valid_mail(mail):
    pattern = r'[a-zA-Z0-9]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, mail)


text = "Contact us at support@example.com or sales@company.org"

print(valid_mail(text))
print(valid_mail("rejuwan@gmail.com"))
