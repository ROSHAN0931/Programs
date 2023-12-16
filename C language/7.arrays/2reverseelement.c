#include <stdio.h>
int main()
{
    int i, n, a[100];
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    for (i = 0; i < n; i++)
    {
        printf("%d", a[i]);
    }
    printf("\n");
    for (i = n - 1; i >= 0; i--)
    {
        printf("%d", a[i]);
    }
    printf("\n");
}