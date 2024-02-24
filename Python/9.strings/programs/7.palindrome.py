# Create a program that checks if a given string is a palindrome.

a=input("Enter string : ")
b=a.lower() #small letters
c=b[::-1] #reverse

if a==c:
    print("palindrome")
else:
    print("not palindrome")