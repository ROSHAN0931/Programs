#include <stdio.h>
int main()
{
    int a = 5;
    int b = 2;
    int sum = a + b;
    int sub = a - b;
    int mul = a * b;
    int div = a / b;
    int mod = a % b;

    printf("%d\nsum is ", sum);
    printf("%d\nsub is ", sub);
    printf("%d\nmul is ", mul);
    printf("%d\ndiv is ", div);
    printf("%d\nmod is", mod);
}