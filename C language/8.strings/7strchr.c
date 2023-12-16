#include<stdio.h>
#include<string.h>
int main()
{
    char a[]="roshan";
    char b='l';
    if(strchr(a,b))
    {
        printf("present");
    }
    else
    {
        printf("not");
    }
}