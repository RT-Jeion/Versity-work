def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    len_nums = len(numbers)
    mid = len_nums // 2

    if len_nums % 2 == 0:
        median = (sorted_numbers[mid -1] + sorted_numbers[mid]) / 2
    else:
        median = sorted_numbers[mid]
    return median, sorted_numbers, mid, len_nums 


nums1 = [3,4,6,7,3,8,3,4,8,6]
nums2 = [6,3,8,1,3,6,3,8,9]

nums1_result = calculate_median(nums1)
nums2_result = calculate_median(nums2)

print(f"Given numbers: {nums1}")
print(f"Sorted Version: {nums1_result[1]}")
print(f"Length of the List: {nums1_result[3]}. Middle Index {nums1_result[2]}")
print(f"Median: {nums1_result[0]}")

print(f"\nGiven numbers: {nums2}")
print(f"Sorted Version: {nums2_result[1]}")
print(f"Length of the List: {nums2_result[3]}. Middle Index {nums2_result[2]}")
print(f"Median: {nums2_result[0]}")
