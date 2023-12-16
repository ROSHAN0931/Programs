#include <stdio.h>
#include <string.h>
int main()
{
    char a[] = "My name is ";
    char b[] = "RODEEKS";
    printf("Before concatenation\n");
    printf("%s\n", a);
    printf("%s\n", b);

    strcat(a, b);

    printf("After concatenation\n");
    printf("%s", a);
}