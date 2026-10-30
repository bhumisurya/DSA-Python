a = [1,2,3,4,6]

n = len(a) + 1

expected_sum = n * (n + 1) // 2
actual_sum = sum(a)

missing = expected_sum - actual_sum

print("The missing number is:", missing)

