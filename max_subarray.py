def max_subarray(nums):
    if not nums:
        return None

    current = nums[0]
    maximum = nums[0]

    for n in nums[1:]:
        current = max(n, current + n)
        maximum = max(maximum, current)

    return maximum

print(max_subarray([1,-4,-5,-9,30,5,6,7,8,9,10,-6,-5,-3,-4,-5]))
