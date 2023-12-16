#include<stdio.h>
#include<string.h>
int main()
{
    char a[]="my name is roshan";
    char b[]="rohan";
    if(strstr(a,b))
    {
        printf("present");
    }
    else
    {
        printf("not");
    }
}