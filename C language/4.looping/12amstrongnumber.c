#include <stdio.h>
#include <math.h>

int main()
{
    int num, len = 0, i, temp, sum = 0;

    printf("Please enter an integer: "); // Taking the user input
    scanf("%d", &num);
    for (i = num; i > 0; i = i / 10)
        len++;
    temp = num;
    while (num > 0)
    {
        sum = sum + pow(num % 10, len);
        num = num / 10;
    }
    if (temp == sum)
    {
        printf("amstrong number");
    }
    else
    {
        printf("not an amstrong number");
    }
}