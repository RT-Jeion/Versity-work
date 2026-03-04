nums = []
while True:

    x = input()
    try:
        x = int(x)
        nums.append(x)
    except:
        break
nums_sum = 0
for i in nums:
    nums_sum += i

median = nums_sum / len(nums)

print(median)