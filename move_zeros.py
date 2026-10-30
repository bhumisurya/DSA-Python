def move_zeroes(nums):
    non_zeros = [x for x in nums if x != 0]
    zeros = nums.count(0)

    return non_zeros + [0] * zeros
print(move_zeroes([1,0,8,6,0,9,0,8]))