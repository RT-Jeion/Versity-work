nums = []
nums_count = input("Type the Total number count you want to add: ")

for i in range(int(nums_count)):
    num = int(input(f"Enter the number {i+1}: "))
    nums.append(num)

nums_sum = 0
for i in nums:
    nums_sum += i

median = nums_sum / len(nums)

print(f"\nThe List of input number is:\n{nums}")
print(f"Median of the Numbers: {median}")