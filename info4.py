t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int,input().split()))
    values = set(arr)
    possible = False



    for x in arr:
        if x + k in values:
            possible = True
            break
if possible:
    print("YES")
else:
    print("NO")