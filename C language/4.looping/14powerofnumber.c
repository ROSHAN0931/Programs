#include <stdio.h>
#include <math.h>
int main()
{
    int b, e;
    printf("enter the number : \n");
    scanf("%d%d", &b, &e);
    int res;

    res = pow(b, e);
    printf("%d", res);
}