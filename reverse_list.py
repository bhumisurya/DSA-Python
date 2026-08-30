lst = list(map(int, input("List: ").split()))

rev = []

for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])
print("Reverse String: ", rev)