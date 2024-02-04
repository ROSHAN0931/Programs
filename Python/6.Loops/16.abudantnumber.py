a=int(input("enter number: "))
s=0

for i in range(1,a):
    if a%i==0:
        s=s+i
    
if s>a:
    print("abudant number")
else:
    print("not abudant number")
    
# 12=1+2+3+4+6