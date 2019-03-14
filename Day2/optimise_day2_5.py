nums = [1,2,3,4,5]
n = len(nums)
left, right, result = [1] * n, [1] * n, [1] * n

for i in range(1, len(nums)):
    left[i] = nums[i - 1] * left[i - 1]

for i in range(len(nums) - 2, -1, -1):
    right[i] = right[i + 1] * nums[i + 1]

print(left)
print(right)

for i in range(0, len(nums)):
    result[i] = left[i] * right[i]

print(result)