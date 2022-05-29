#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct c
{
    float x;
    float y;
};

int main() {
    int n, fac;
    float ugol;
    struct c z;

    printf_s("Enter x, y: \n");
    scanf_s("%fac", &z.x);
    scanf_s("%fac", &z.y);

    printf_s("Enter n: \n");
    scanf_s("%d", &n);

    ugol = z.y / z.x;
    z.x = 1;
    z.y = 1;
    for (int i = 1; i < n; i++) {
        fac = 1;
        if (i != 0)
            fac = fac * i;
        z.x += 1 / fac * cos(i * ugol);
        z.y += 1 / fac * sin(i * ugol);
    }
    printf_s("exp(z) = %f + %fi", z.x, z.y);
    return 0;
}