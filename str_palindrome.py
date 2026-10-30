s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
if rev == s:
    print("String is Palindrome")
else:
    print("Not Palindrome")