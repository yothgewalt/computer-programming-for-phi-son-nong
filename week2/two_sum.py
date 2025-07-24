def two_sum(nums, target):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
            
    return []
            
n = two_sum([1, 2, 3, 7, 8], 10)
print(n)