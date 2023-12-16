
// with arguements and without return type

#include <stdio.h>
void printstar(int a);

int main()
{
    printstar(20);
    printf("\n \t \t WELCOME \n");
    printstar(70);
}

void printstar(int a)
{
    for (int i = 1; i <= a; i++)
    {
        printf("* ");
    }
}