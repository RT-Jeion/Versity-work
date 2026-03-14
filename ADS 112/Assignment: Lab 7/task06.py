# Write a Python program that removes duplicate values from a list using a set.

nums_list = [2,4,7,2,8,4,5,6,2,3,5,3,6]

nums_set = set(nums_list)

new_list = list(nums_set)

print("Given List:", nums_list)
print("New list after removing the duplicates:", new_list)
