#include <stdio.h>
int main()
{

    // draw rectangle and square
    int n, m;
    printf("Enter the input : ");
    scanf("%d", &n);
    printf("Enter the input : ");
    scanf("%d", &m);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("* ");
        }
        printf("\n");
    }
}