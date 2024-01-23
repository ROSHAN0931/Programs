
a=int(input("Enter number\n"))
b=int(input("Enter number\n"))
c=int(input("Enter number\n"))

if a<b and a<c:
    l=a
elif b<c and b<a:
    l=b
else:
    l=c

if a>b and a>c:
    g=a
elif b>c and b>a:
    g=b
else:
    g=c
    
m=a+b+c-l-g

print(l,m,g)
