arr = [1,2,3,4,3,2,1,3,4,5,5,6,7,3,2,1,3,4]
unique = []
for i in arr:
    if i not in unique:
        unique.append(i)
print(unique)
