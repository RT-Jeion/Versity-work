# Implement a function that calculates the intersection of multiple sets

def intersection_of_sets(*sets):
    if not sets:
        return set()

    return set.intersection(*sets)

set1 = {1, 2, 3, 4}
set2 = {2, 3, 4, 5}
set3 = {3, 4, 5, 6}
set4 = {3, 4, 5, 6, 7}

print("Set no.1", set1)
print("Set no.2", set2)
print("Set no.3", set3)
print("Set no.4", set4)

result = intersection_of_sets(set1, set2, set3, set4)
print(f"Intersection of individual sets: {result}")
