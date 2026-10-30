def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


print(is_sorted([3,4,5,6]))
print(is_sorted([12,23,3,4,5,6]))


