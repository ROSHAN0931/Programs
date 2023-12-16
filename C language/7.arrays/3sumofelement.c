#include <stdio.h>
void main()
{
    int a[100];
    int i, n, sum = 0;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    for (i = 0; i < n; i++)
    {
        sum += a[i];
    }
    printf("%d", sum);
}