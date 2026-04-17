# Write a Python program that checks if a string is a valid credit card number using Luhn’s algorithm and regex.

import re

def check_valid_card(card_number: str):

    pattern = r"^(4|5|6)\d{3}-?\d{4}-?\d{4}-?\d{4}$"

    if not re.match(pattern, card_number):
        return False
    
    cleaned_number = card_number.replace("-", "")
    
    # Only converts the character if it is a digit
    num_list = [int(i) for i in str(cleaned_number) if i.isdigit()]

    for i in range(len(num_list) - 2, -1, -2):
        num_list[i] = num_list[i] * 2
        if num_list[i] > 9:
            num_list[i] = int(str(i)[0]) + int(str(i)[1])
    
    if sum(num_list) % 10 == 0:
        return True
    return False


test_card = "4242-4242-4242-4242"


print(check_valid_card(test_card))
