#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main()
{
    char a[] = "roSHAn";
    printf("%s\n", strlwr(a));
    puts(strupr(a));

    char b[] = "roshan";
    printf("%c\n", toupper(b[2]));

    char c = 'Z';
    printf("%c\n", tolower(c));

    if (isalpha(c))
    {
        puts("alpha");
    }
    else
    {
        puts("not");
    }
}