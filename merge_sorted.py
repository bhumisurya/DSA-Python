def merge_sorted(a,b):
    i = 0
    j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])

    return result

a = sorted([4,3,2,1,6])
b = sorted([8,7,6,5,4,3])

print(merge_sorted(a,b))