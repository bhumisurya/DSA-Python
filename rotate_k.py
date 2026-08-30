lst = list(map(int, input("list: ").split()))

k = 2

k = k % len(lst)

result = lst[-k:] + lst[:-k]

print(result)

