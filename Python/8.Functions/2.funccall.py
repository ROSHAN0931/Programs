
#Get input from user and pass it to a function and display even or odd:-

def evenodd(a):
    if a%2==0:
        print("even")
    else:
        print("odd")
a=int(input())
evenodd(a)

# Get 2 input from user pass to fun and print the numbers from range

def printrange(a,b):
    for i in range(a,b):
        print(i)

a=int(input())
b=int(input())
printrange(a,b)
