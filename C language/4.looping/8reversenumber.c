#include <stdio.h>
int main()
{
    int a;
    int rem, b = 0;
    printf("Enter the number : ");
    scanf("%d", &a);
    while (a != 0)
    {
        rem = a % 10;
        b = b * 10 + rem;
        a = a / 10;
    }
    printf("%d", b);
}