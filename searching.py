arr = [10,40,50,30,20,100]

target = int(input("Target: "))

if target in arr:
    for i in range(len(arr)):
        if arr[i] == target:
            print("Found at Index of Target:", i)
            break
else:
    print("Not Found...")

