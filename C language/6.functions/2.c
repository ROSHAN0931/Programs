
// without arguements and without return type

#include <stdio.h>
void printstar();

int main()
{
    printf("print the star :");
    printstar();
}

void printstar()
{
    int a;
    scanf("%d", &a);
    for (int i = 1; i <= a; i++)
    {
        printf("* ");
    }
}