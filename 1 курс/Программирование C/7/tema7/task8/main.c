#include <stdio.h>
#include <stdlib.h>

int main() {
    int a,r,h;
    float sq;
    printf("Enter num: \n");
    scanf_s("%d", &a);
    switch(a){
        case 1:
            printf("Krug, enter R");
            scanf_s("%d",&r);
            sq=r*r*3,14;
            printf("%f\n", sq);
            break;
        case 2:
            printf("Obiem shara, enter R");
            scanf_s("%d",&r);
            sq=4/3*3,14*r*r*r;
            printf("%f\n", sq);
            break;
        case 3:
            printf("Obiem silindra, enter R, h");
            scanf_s("%d %d",&r, &h);
            sq=3,14*r*r*h;
            printf("%f\n", sq);
            break;
        case 4:
            printf("Ploshad sferi, enter R");
            scanf_s("%d",&r);
            sq=4*3,14*r*r;
            printf("%f\n", sq);
            break;
        default:
            printf("Wrong enter");
    }
    return 0;
}