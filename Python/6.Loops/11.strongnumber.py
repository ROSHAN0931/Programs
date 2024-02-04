a=int(input("enter number: "))
s=0
t=a
while a>0:
    i=0
    f=1
    r=a%10
    while r>0:
        f=f*r
        r=r-1
    a=a//10
    s=s+f    
    
print(s)
if s==t:
    print("strong number")
else:
    print("not a strong number")
    
# 145=1!+4!+5!