num = int(input("Enter a number: "))
org = num
reverse = 0
while org > 0:
    digit = org % 10
    reverse = (reverse * 10) + digit
    org = org // 10 

if num == reverse:
    print("Palindrome....")

else:
    print("NOT Palindrome....")

    