def calculate_median(numbers):
    # Sort numbers first so median position can be found correctly.
    sorted_numbers = sorted(numbers)
    # Total item count and middle index used for both odd/even logic.
    len_nums = len(numbers)
    mid = len_nums // 2

    # For even-sized lists, median is the average of the two center values.
    if len_nums % 2 == 0:
        median = (sorted_numbers[mid -1] + sorted_numbers[mid]) / 2
    # For odd-sized lists, median is the center value directly.
    else:
        median = sorted_numbers[mid]
    return median, sorted_numbers, mid, len_nums 


# Example input lists.
nums1 = [3,4,6,7,3,8,3,4,8,6]
nums2 = [6,3,8,1,3,6,3,8,9]

# Compute median details for each list.
nums1_result = calculate_median(nums1)
nums2_result = calculate_median(nums2)

# Display results for first list.
print(f"Given numbers: {nums1}")
print(f"Sorted Version: {nums1_result[1]}")
print(f"Length of the List: {nums1_result[3]}. Middle Index {nums1_result[2]}")
print(f"Median: {nums1_result[0]}")

# Display results for second list.
print(f"\nGiven numbers: {nums2}")
print(f"Sorted Version: {nums2_result[1]}")
print(f"Length of the List: {nums2_result[3]}. Middle Index {nums2_result[2]}")
print(f"Median: {nums2_result[0]}")
