// METHOD 1:

// Note : gets() has been removed from c11. So it might give you a warning when implemented.
// We see here that it doesn’t bother about the size of the array.
// So, there is a chance of Buffer Overflow.

#include <stdio.h>
int main()
{
    char str[20];
    gets(str);
    printf("%s", str);
    return 0;
}

// METHOD 2:

// To overcome the above limitation, we can use fgets as :
// Syntax : char *fgets(char *str, int size, FILE *stream)
// Example : fgets(str, 20, stdin); as here, 20 is MAX_LIMIT according to declaration.

#include <stdio.h>
#define MAX_LIMIT 20
int main()
{
    char str[MAX_LIMIT];
    fgets(str, MAX_LIMIT, stdin);
    printf("%s", str);
    return 0;
}

// METHOD 3:

// Using %[^\n]%*c inside scanf
// Example : scanf(“%[^\n]%*c”, str);

#include <stdio.h>
int main()
{
    char str[20];
    scanf("%[^\n]%*c", str);
    printf("%s", str);
    return 0;
}

// METHOD 4:

// Using %[^\n]s inside scanf.
// Example :  scanf(“%[^\n]s”, str);

#include <stdio.h>
int main()
{
    char str[100];
    scanf("%[^\n]s", str);
    printf("%s", str);
    return 0;
}
