lst = list(map(int,input("List: ").split()))

n = len(lst)+1

expected_sum = n * (n + 1) // 2

actual_sum = sum(lst)

missing_no = expected_sum - actual_sum

print("Missing number is: ",missing_no)

