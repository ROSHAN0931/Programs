#include <stdio.h>
int main()
{
    int age = 22;
    int wei = 55;

    if (age >= 18 && wei >= 50)
    {
        printf("Eligible\n");
    }
    if (age > 24 || wei > 30)
    {
        printf("partially eligible\n");
    }
    else
    {
        printf("Not eligible");
    }
}