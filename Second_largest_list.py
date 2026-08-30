lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("List: ",lst)
largest = float("-inf")
second_largest = float("-inf")

for i in lst:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print("Second Largest Number from List: ",second_largest)
