lst = list(map(int, input("Elements of list: ").split()))
print(lst)

freq = {}
for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)