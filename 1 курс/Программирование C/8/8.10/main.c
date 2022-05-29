#include<stdlib.h>
#include<stdio.h>
#include<math.h>

double speed(float d)
{
    double h = 6.626e-34;
    double m = 9.1e-31;
    double c = 2.9980e+8;
    double l = 2.5e-7;
    d = d*1.602e-19;
    double v = sqrt( 2/m * ( h*c/l - d));
    return v;
}

int main()
{
    printf("Speed silver: %.6f\n", speed(4.3));
    printf("Speed nickel: %.6f", speed(4.94));
    return 0;
}
