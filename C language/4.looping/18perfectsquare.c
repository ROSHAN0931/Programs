#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
    int n;
    printf("enter the number : ");
    scanf("%d", &n);
    int temp = n;
    int sum = 0;
    for (int i = 1; i < n; i++)
    {
        if (n % i == 0)
        {
            sum = sum + i;
        }
    }
    if (temp == sum)
    {
        printf("perfect square");
    }
    else
    {
        printf("not a perfect square");
    }
}