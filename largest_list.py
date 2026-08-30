lst = list(map(int, input("Enter the elements with space: ").split()))
print("List: ")
max_no = lst[0]

for i in lst:
    if i > max_no:
        max_no = i
print("Largest Number: ",max_no)