t = int(input())

for _ in range(t):
    n , k = map(int,input().split())
    s = input().strip()

    white_count = s[:k].count('W')
    white_min = white_count

    for i in range(n , k):
        if s[ i-k] == 'W':
            white_count -= 1

        if s[ i] == 'W':
            white_count += 1

            white_min = min(white_count, white_min)

        

print(white_min)



