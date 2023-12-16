#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
    int n;
    printf("enter the number : ");
    scanf("%d", &n);
    int sq = n * n;
    int temp = 1;
    while (n > 0)
    {
        if (n % 10 != sq % 10)
        {
            temp = 0;
            printf("not automorphic");
            break;
        }
        n /= 10;
        sq /= 10;
    }
    if (temp == 1)
    {
        printf("automorphic number");
    }
}