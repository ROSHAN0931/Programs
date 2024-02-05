a=40
b=224

s1=0
s2=0

for i in range(1,a):
    if a%i==0:
        s1=s1+i
        
for i in range(1,b):
    if b%i==0:
        s2=s2+i
        
if ((s1//a)==(s2//b)):
    print("friendly pair")
else:
    print("not")
