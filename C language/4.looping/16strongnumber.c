#include <stdio.h>
int main()
{
    int n;
    printf("enter the number : ");
    scanf("%d", &n);
    int fact;
    int temp = n;
    int i, rem, sum = 0;
    while (n)
    {
        i = 1;
        fact = 1;
        rem = n % 10;

        while (i <= rem)
        {
            fact = fact * i;
            i++;
        }
        sum = sum + fact;
        n = n / 10;
    }

    if (sum == temp)
    {
        printf("strong number");
    }
    else
    {
        printf("not a strong number");
    }
}