def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

nums = list(map(int,input("nums: ").split()))
target = int(input("Target: "))
result = twosum(nums,target)
print(result)