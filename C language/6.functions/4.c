
// without arguements and with return type

#include <stdio.h>
float value();

int main()
{
    float b = value();
    printf("%f", b);
}

float value()
{
    float a;
    printf("enter the decimal value : \n");
    scanf("%f", &a);
    return a;
}