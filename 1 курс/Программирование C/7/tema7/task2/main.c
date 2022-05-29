#include <stdio.h>
#include <stdlib.h>

int main() {
    int a, b, h;
    printf("Enter a, b, h:\n");
    scanf_s("%d %d %d",&a,&b,&h);
    if(h==0){
        a*=b;
        printf("Square: %d",a);
    } else{h*=(a+b)/2;
        printf("Square: %d",h);}
    return 0;
}