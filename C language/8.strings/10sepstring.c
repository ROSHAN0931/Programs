#include <stdio.h>
int main()
{
    char a[100];
    gets(a);
    int b = 0;
    printf("before seperating : %s\n", a);
    printf("after seperating : ");
    while (a[b] != '\0')
    {
        printf("%c ", a[b]);
        b++;
    }
    return 0;
}
