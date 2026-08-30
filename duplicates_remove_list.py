lst = list(map(int, input("List: ").split()))

unique = []

for item in lst:
    if item not in unique:
        unique.append(item)

print("Unique Elements in List: ",unique)
