#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
    int n;
    printf("enter the number : ");
    scanf("%d", &n);
    int sum = 0;
    int temp = n;
    for (int i = 1; i < n; i++)
    {
        if (n % i == 0)
        {
            sum += i;
        }
    }
    if (sum > temp)
    {
        printf("abudant number");
    }
    else
    {
        printf("not abudant number");
    }
}