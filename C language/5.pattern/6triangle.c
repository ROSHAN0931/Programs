#include <stdio.h>
int main()
{
    int n, i, j, sp;
    printf("Input number of rows : ");
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        for (sp = 1; sp <= n - i; sp++)
        {
            printf("  ");
        }
        for (j = 1; j <= 2 * i - 1; j++)
        {
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}