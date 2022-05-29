#include <stdio.h>
#include <stdlib.h>

int fac(int a){
    if(a==0){
        return 1;
    }
    else
        return fac(a-1)*a;
}

int main() {
    int a;
    printf("Enter num: \n");
    scanf_s("%d", &a);
    printf("%d!=%d\n",a, fac(a));
    return 0;
}