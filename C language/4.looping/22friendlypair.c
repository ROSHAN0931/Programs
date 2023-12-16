#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
    int a, b;
    printf("enter the number : \n");
    scanf("%d%d", &a, &b);
    int sum1 = 0;
    int sum2 = 0;
    int div1, div2;
    for (int i = 1; i < a; i++)
    {
        if (a % i == 0)
        {
            sum1 += i;
        }
    }
    for (int j = 1; j < b; j++)
    {
        if (b % j == 0)
        {
            sum2 += j;
        }
    }
    if ((sum1 / a) == (sum2 / b))
    {
        printf("friendly pair");
    }
    else
    {
        printf("not friendly pair");
    }
}