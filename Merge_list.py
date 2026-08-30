l1 = list(map(int,input("List 1: ").replace(","," ").split()))
l2 = list(map(int,input("List 2: ").replace(","," ").split()))

merge = []

for i in l1:
    merge.append(i)
for i in l2:
    merge.append(i)

print("Merged List: ",merge)