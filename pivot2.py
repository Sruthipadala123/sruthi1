nums = input()
def pivot(nums):
    total = sum(nums)
    left = 0
    for i,num in nums:
        right = total - left -num
    if left == right:
         return i
    left += num
    return -1
result = pivot(nums)
print("pivot :",result)
