def max_sum(arr, k):
    maximum = float("-inf")

    for i in range(len(arr) - k + 1):
        current_sum = 0

        for j in range(i, i + k):
            current_sum += arr[j]

            maximum = max(maximum, current_sum)

    return maximum
print(max_sum([2,3,4,5,1,3,4,2,6,7],3))