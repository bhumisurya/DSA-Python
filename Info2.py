t = int(input())

for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())

    suneet_order = [(a1,a2),(a2,a1)]
    slavic_order = [(b1,b2),(b2,b1)]
    
    wins = 0

    for s in suneet_order:
        for b in slavic_order:
            sumit_win = 0
            slavic_win = 0

        if s[0] > b[0]:
            sumit_win += 1
        elif s[0] < b[0]:
            slavic_win += 1

        if s[1] > b[1]:
            sumit_win += 1
        elif s[1] < b[1]:
            slavic_win += 1

        if sumit_win > slavic_win:
            wins += 1

print("Wins of Suneet: ",wins)

        

