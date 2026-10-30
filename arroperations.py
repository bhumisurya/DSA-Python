arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Insertion
arr.append(40)
print("arr.append(40): ", arr)
arr.insert(3, 700)
print("arr.insert(3, 700): ", arr)

# Deletion
arr.remove(10)  # by value
print("arr.remove(10): ", arr)
del arr[3]  # by index
print("del arr[3]: ", arr)

# Maximum & Minimum
print("min(arr): ", min(arr))
print("max(arr): ", max(arr))

maximum = arr[0]
for x in arr:
    if x > maximum:
        maximum = x
print("Maximum: ", maximum)

# Duplicates
if len(arr) != len(set(arr)):
    print("Array containing Duplicates")
else:
    print("No Duplicates")

#frequency
freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1
print(freq)

#two sum
a = [1,2,3,4,2,1,3,4,5,6,7]
target = 7
seen = set()
for x in a:
    if target - x in seen:
        print("Pair Found..")
        break
    seen.add(x)
