#fibonacci
n = int(input("Enter number of terms: "))

a = 0
b = 1

for _ in range(n):
    print(a, end=" ") #for printing in one line , to not move next line 

    temp = a
    a = b
    b = temp + b

