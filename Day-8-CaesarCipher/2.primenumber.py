
def prime(number):
    isprime=True
    for i in range(2,number):
        if number % i==0:
            isprime=False
    if isprime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n=int(input())
prime(number=n)