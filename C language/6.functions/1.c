
// with arguemets and with return type

#include <stdio.h>
int res(int, int); // function declaration

int main()
{
    int a, b;
    printf("enter the value \n");
    scanf("%d%d", &a, &b);
    int c = res(a, b); // function call // actual arguements
    printf("%d", c);
}

// function definition
int res(int x, int y) // formal arguements
{
    int z = x + y;
    return z;
}