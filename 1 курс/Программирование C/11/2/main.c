#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct vector
{
    char name;
    int x;
    int y;
    int z;
};

int main()
{
    int x,y,z;
    struct vector a;
    struct vector b;
    a.name='a';
    a.x=1;
    a.y=2;
    a.z=3;

    b.name='b';
    b.x=4;
    b.y=5;
    b.z=6;
    printf_s("%c = {%d; %d; %d;}\n", a.name, a.x, a.y, a.z);
    printf_s("%c = {%d; %d; %d;}\n", b.name, b.x, b.y, b.z);
    printf_s("Skalyar %d\n", a.x*b.x + a.y*b.y + a.z*b.z);

    x = a.y*b.z - a.z*b.y;
    y = -(a.x*b.z - a.z*b.x);
    z = a.x*b.y - a.y*b.x;

    printf_s("Vektornoye proizvedeniye {%d; %d; %d}\n", x, y, z);
    printf_s("Absolute %c = %lf\n", a.name, sqrt(a.x*a.x + a.y*a.y + a.z*a.z));
    printf_s("Absolute %c = %lf", b.name, sqrt(b.x*b.x + b.y*b.y + b.z*b.z));

    return 0;
}
