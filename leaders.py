def leader(arr):
    res = []
    n = len(arr)

    maxRight = arr[-1]

    res.append(maxRight)

    for i in range(n - 2, -1, -1):
        if arr[i] >= maxRight:
            maxRight = arr[i]
            res.append(maxRight)

    res.reverse()

    return res

print(leader([54,3,4,5,23,9,7,7,8,10]))
