n = int(input("Number:"))
original = n
index = len(str(n))
total = 0
while n > 0:
    digit = n % 10
    total += digit ** index
    n = n // 10
if original == total:
    print("Armstrong")
else:
    print("NOT")