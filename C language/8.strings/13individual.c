#include <stdio.h>
#include <string.h>
int main()
{
    char a[100];
    gets(a);
    int i = 0;
    while (a[i] != '\0')
    {
        printf("%c ", a[i]);
        i++;
    }
}