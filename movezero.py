arr = [1,0,0,9,8,7,6,0,0,0,0,0,8,8,7,6,5,5,3,4,4,4,4,4]

position = 0

for num in arr:
    if num != 0:
        arr[position] = num
        position += 1

while position < len(arr):
    arr[position] = 0
    position += 1
print(arr)