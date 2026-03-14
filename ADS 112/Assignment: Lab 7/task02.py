# Create a set of integers and implement  a function that returns the difference between the maximum and minimum values in the set.

def max_min_dif(int_set):
    int_list = list(int_set)
    return int_list[-1] - int_list[0]

nums_set = {8,3,4,1,7,2,9,5}
max_min_value_diff = max_min_dif(nums_set)
print("Set of Integrts:", nums_set)
print("Difference between the maximum and minimum values in the set: ",max_min_value_diff)
