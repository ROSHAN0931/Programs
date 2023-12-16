#include <stdio.h>
#include <string.h>
int main()
{
    char a[100];
    gets(a);
    int i = 0;
    int w = 1;
    while (a[i] != '\0')
    {
        if (a[i] == ' ' || a[i] == '\n' || a[i] == '\0')
        {
            w++;
        }
        i++;
    }
    printf("Total number of words in given string is %d", w);
}