def ContainsDuplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)

    return False

nums = list(map(int, input("Elements: ").split()))

result = ContainsDuplicate(nums)
print(result)