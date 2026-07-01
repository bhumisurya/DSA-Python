n = int(input("Number: "))

def Prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
                
    return True

if Prime(n):
    print("Prime number")

else:
    print("Not Prime number")

#Hello 

m = int(input("Number: "))
if (m % 2 == 0 and m % 3 == 0):
    print("Not Prime number")
else:
    print("Prime number")