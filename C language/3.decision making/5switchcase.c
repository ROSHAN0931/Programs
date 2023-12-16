#include <stdio.h>
int main()
{
    char place;
    scanf("%c", &place);

    switch (place)
    {
    case 'o':
        printf("ooty");
        break;

    case 'c':
        printf("coimbatore");
        break;

    case 't':
        printf("tirupati");
        break;

    case 'm':
        printf("manjoor");
        break;

    default:
        printf("no place found");
    }
}