num = int(input("Enter a number: "))

fact = 0
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)
    
if num < 0:
    print("Can't find factorial of negative no.")

else:
    print("Factorial: ",fact(num))