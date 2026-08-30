lst = list(map(int, input("Enter elements with space: ").split()))
print("List: ",lst)

min_no = lst[0]

for i in lst:
    if i < min_no:
        min_no = i
print("Smallest number: ",min_no)