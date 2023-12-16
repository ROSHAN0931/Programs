#include <stdio.h>
int main()
{
    int scope;
    scanf("%d", &scope);
    if (scope == 8)
    {
        printf("awm,kar98,m24");
    }
    else if (scope == 6)
    {
        printf("m416,scarl,vector,ump");
    }
    else if (scope == 2)
    {
        printf("akm,m762");
    }
    else
    {
        printf("pistol,crossbow,shotgun");
    }
}