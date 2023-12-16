#include <stdio.h>
int main()
{
    int a = 2;
    int b = 5;
    printf("Before swapping : \n");
    printf("%d\n", a);
    printf("%d\n", b);
    int swap = a;
    a = b;
    b = swap;
    printf("After swapping : \n");
    printf("%d\n", a);
    printf("%d", b);
}