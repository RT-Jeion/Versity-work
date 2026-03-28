# Implement a phonebook using a dictionary that can also update the phone number of an existing contact.

import json

phonebook = {}

while True:
    print("\nType [1] to add new contact")
    print("Type [2] to modify existing contact")
    print("Type [3] to show all contacts.")
    print("Type [4] to quit")
    response = input("Enter your response: ")

    if response == "1":
        name = input("Enter name: ")
        number = input("Enter the number: ")
        phonebook[name] = number

    elif response == "2":
        name = input("Enter an existing contact name: ")
        number = input("Enter new contact number: ")
        phonebook[name] = number
    
    elif response == "3":
        print("All Contacts.")
        print(json.dumps(phonebook, indent=1))

    elif response == "4":
        print("System Terminated.")
        break

    else:
        print("Invalid choice")
