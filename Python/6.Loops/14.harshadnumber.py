a=int(input("enter number : "))
s=0
t=a

while a>0:
    r=a%10
    s=s+r
    a=a//10

if t%s==0:
    print("harshad number")
else:
    print("not harshad number")