a=input("enter number: ")
n=int(a)
b=len(a)
t=n
s=0

while n>0:
    r=n%10
    c=pow(r,b)
    n=n//10
    s=s+c
    
if s==t:
    print("amstrong number")
else:
    print("not amstrong number")
    
# 153=1^3+5^3+3^3