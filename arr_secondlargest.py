arr = [12,2,3,4,9,100]

largest = float('-inf')
second_largest = float('-inf')

for i in arr:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print(second_largest)