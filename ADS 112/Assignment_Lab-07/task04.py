# Write a program to merge two sets and print the resulting set.

nums_set1 = {10, 7, 4, 15, 12, 3, 6, 8}
nums_set2 = {11, 9, 2, 13, 17, 14, 16, 5}

resulting_set = set()

for i in nums_set1:
    resulting_set.add(i)

for i in nums_set2:
    resulting_set.add(i)

print("1st Set:", nums_set1)
print("2nd set:", nums_set2)
print("Merged set:",resulting_set)
