# Write a code to count the sum of first 5 natural numbers:-

# a=int(input())
# sum=0
# for i in range(1,a):
#     sum+=i
# print(sum)

# List:-

# a=[]
# a.append(10)
# a.append(20)
# b=input()
# a.append(b)
# print("items in a: ",a)

# Read 10 numbers from the keyboard and find their sum and average:-

a=[]
print("enter 5 numbers : ")
for i in range(5):
    num=int(input("enter num  "+str(i+1)+" "))
    a.append(num)
print(a)

sum=0
count=0
for i in a:
    sum+=i

count=len(a)
print("sum is :",sum)

print("total is : ",count)
average = sum/count
print("average is : ",int(average))