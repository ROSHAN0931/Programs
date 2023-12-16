#include <stdio.h>
int main()
{
    int n, t = 0;
    printf("Enter the number : ");
    scanf("%d", &n);
    // for (int i = 2; i <= n / 2; i++)
    // {
    //     if (n % i == 0)
    //     {
    //         t++;
    //         break;
    //     }
    // }

    // if (t == 0 && n != 1)
    // {
    //     printf("Prime");
    // }
    // else
    // {
    //     printf("Not prime");
    // }

    while (n > 2)
    {
        if (n % 2 == 0)
        {
            t++;
        }
        n++;
    }

    if (t == 0)
    {
        printf("Prime");
    }
    else
    {
        printf("Not prime");
    }
}