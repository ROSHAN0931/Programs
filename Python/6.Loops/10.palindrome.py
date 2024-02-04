a=int(input())
b=0
t=a
while a>0:
    r=a%10
    b=b*10+r
    a=a//10
print(b)

if b==t:
    print("palindrome")
else:
    print("not a palindrome")