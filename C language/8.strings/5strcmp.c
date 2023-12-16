#include <stdio.h>
#include <string.h>
int main()
{
    char a[] = "abcdef";
    char b[] = "abcdef";
    printf("%d\n", strcmp(a, b));

    if (strcmp(a, b) == 0)
    {
        printf("same");
    }
    else
    {
        printf("not same");
    }
}

// 0	if strings are equal
// >0	if the first non-matching character in str1 is greater (in ASCII) than that of str2.
// <0	if the first non-matching character in str1 is lower (in ASCII) than that of str2.