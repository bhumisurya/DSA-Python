l1 = list(map(int,input("List 1: ").replace(","," ").split()))
l2 = list(map(int,input("List 2: ").replace(","," ").split()))

intersect = []

for i in l1:
    if i in l2 and i not in intersect:
        intersect.append(i)
print("Intersection elements: ",intersect)