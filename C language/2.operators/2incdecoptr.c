#include <stdio.h>
int main()
{
    int a = 5;
    int posin = a++;
    printf("posin is %d\n", posin);

    int b = 3;
    int prein = ++b;
    printf("prein is %d\n", prein);

    int c = 10;
    int posde = c--;
    printf("posde is %d\n", posde);

    int d = 34;
    int prede = --d;
    printf("prede is %d\n", prede);

    int e = 5;
    int equation = e++ + ++e + e++ + ++e;
    printf("Answer is %d", equation);
}