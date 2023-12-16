#include <stdio.h>
int main()
{
    int n;
    printf("Enter the number n :");
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        if (i == 5)
        {
            continue;
        }
        printf("%d\n", i);
    }
}