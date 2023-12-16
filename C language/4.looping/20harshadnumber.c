#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
    int n;
    printf("enter the number : ");
    scanf("%d", &n);
    int temp = n;
    int rem, sum = 0;
    while (n > 0)
    {
        rem = n % 10;
        sum += rem;
        n /= 10;
    }
    if (temp % sum == 0)
    {
        printf("harshad number");
    }
    else
    {
        printf("not harshad number");
    }
}