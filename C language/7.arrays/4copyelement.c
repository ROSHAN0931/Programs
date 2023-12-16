#include <stdio.h>
int main()
{
    int arr1[100], arr2[100];
    int i, n;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        printf("element - %d : ", i);
        scanf("%d", &arr1[i]);
    }

    for (i = 0; i < n; i++)
    {
        arr2[i] = arr1[i];
    }

    for (i = 0; i < n; i++)
    {
        printf("%d", arr1[i]);
    }
    printf("\n");

    for (i = 0; i < n; i++)
    {
        printf("%d", arr2[i]);
    }
}
