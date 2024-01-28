# Print the even numbers between 1 to 10:-

a=int(input())
b=int(input())

for i in range(a,b):
    if i%2==0:
        print(i)
        
# Count the number of odd numbers from 1 to 10:-

a=int(input())
b=int(input())
count=0
for i in range(a,b):
    if i%2!=0:
        count+=1        
print(count)

# Count the number of odd and even numbers from 1 to 10:-

a=int(input())
b=int(input())
even=0
odd=0
for i in range(a,b):
    if i%2!=0:
        even+=1
    else:
        odd+=1
print("even",even)
print("odd",odd)