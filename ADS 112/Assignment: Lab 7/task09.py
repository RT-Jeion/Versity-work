# Create a function that finds the union of multiple dictionaries (merging key-value pairs).

def dict_union(*dicts):
    merged_dict = {}

    for d in dicts:
        merged_dict |= d

    return merged_dict

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d3 = {'d': 5, 'a': 6}

result = dict_union(d1,d2,d3)

print("1st Dict:",d1)
print("2nd Dict:",d2)
print("3rd Dict:",d3)
print("Merged Dict:", result)
