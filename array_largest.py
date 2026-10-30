arr = [12,34,54,2,3,4,5,2,1]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num
print(largest)