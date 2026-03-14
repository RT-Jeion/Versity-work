# Implement a program that counts the 
# frequency of each character in a string using a dictionary

result = {}

s = input("Enter the String: ")

for i in s:
    if i in result.keys():
        result[i] += 1
    else:
        result[i] = 1

print("Given String:", s)
print(result)
