#include <stdio.h>
int main()
{
    float d = 3.44556;
    printf("%f\n", d);   // after decimal point 6 places will be there
    printf("%.f\n", d);  // print as an integer
    printf("%.1f\n", d); // print 1 value after decimal point
    printf("%.2f\n", d); // print 2 value after decimal point
}