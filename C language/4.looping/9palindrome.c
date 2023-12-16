#include <stdio.h>
int main()
{
    int a;
    int rem, temp, rev = 0;
    printf("Enter the number : ");
    scanf("%d", &a);
    temp = a;
    while (temp != 0)
    {
        rem = temp % 10;
        rev = rev * 10 + rem;
        temp = temp / 10;
    }

    if (a == rev)
    {
        printf("Palindrome");
    }
    else
    {
        printf("Not a palindrome");
    }
}