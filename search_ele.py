lst = list(map(int, input("List: ").split()))

key = int(input("Enter the key to search: "))
found = False
for i in lst:
    if i == key:
        found = True
        break
print(found)
