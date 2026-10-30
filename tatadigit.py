def find_no(m, s):
    if s == 0:
        if m == 1:
            return "0","0"
        else:
            return "-1","-1"

    if m > 9 * m:
        return "-1","-1"

    #Largest number
    remaining = s
    largest = ""

    for i in range(m):
        digit = min(9, remaining)
        largest += str(digit)
        remaining -= digit

    #smallest number
    remaining = s
    smallest = ""
    for i in range(m):
        if i == 0:
            digit = max(1, remaining - 9 * (m - 1))
        else:
            digit = max(0, remaining - 9 * (m - i - 1))

    return largest, smallest

m, s = map(int, input().split())
largest, smallest = find_no(m, s)
print(largest, smallest)
