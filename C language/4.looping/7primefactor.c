#include <stdio.h>
int main()
{
    int n, tem;
    printf("Enter the number : ");
    scanf("%d", &n);
    for (int i = 2; i <= n / 2; i++)
    {
        if (n % i == 0)
        {
            tem = 1;

            for (int j = 2; j <= i / 2; j++)
            {
                if (i % j == 0)
                {
                    tem = 0;
                    break;
                }
            }
            if (tem == 1)
            {
                printf("%d ", i);
            }
        }
    }
}