nums = []
nums_count = input("Type the Total number count you want to add: ")

for i in range(int(nums_count)):
    num = int(input(f"Enter the number {i+1}: "))       # taking the numbers as input and type casting in Integer values
    nums.append(num)        # putting the vales in a list

nums_sum = 0
for i in nums:
    nums_sum += i      # addition of all numbers of the list

median = nums_sum / len(nums)    # addition of all numbers divided by the length of the List


print(f"\nThe List of input number is:\n{nums}")
print(f"Median of the Numbers: {median}")