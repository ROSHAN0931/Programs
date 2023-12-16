#include <stdio.h>
int main()
{
    int n;
    printf("enter the number : ");
    scanf("%d", &n);
    int a = 0, b = 1;
    printf("%d %d ", a, b);
    int fib;
    for (int i = 2; i < n; i++)
    {
        fib = a + b;
        a = b;
        b = fib;
        printf("%d ", fib);
    }
}