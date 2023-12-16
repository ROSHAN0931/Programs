#include <stdio.h>
int main()
{
    int n;
    int rev = 0, sum = 0;
    printf("enter the number : ");
    scanf("%d", &n);
    while (n != 0)
    {
        sum = sum + n % 10;
        n = n / 10;
    }
    printf("%d", sum);
}