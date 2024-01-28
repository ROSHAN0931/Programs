# Count the number which is divisible by 3 and 5 from 1-100:-

a=int(input())
b=int(input())
count=0
for i in range(a,b):
    if i%3==0 and i%5==0:
        count+=1        
print(count)