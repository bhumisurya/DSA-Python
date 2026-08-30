l1 = list(map(int,input("List 1: ").replace(","," ").split()))
l2 = list(map(int,input("List 2: ").replace(","," ").split()))

union = []

for i in l2:
    if i not in union:
        union.append(i)
print("Union of Two Lists: ",union)