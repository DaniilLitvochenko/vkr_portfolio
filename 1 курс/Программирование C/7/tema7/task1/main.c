#include <stdio.h>
#include <stdlib.h>

int main() {
    int a,b,c;
    printf("Enter 3 nums: \n");
    scanf_s("%d %d %d", &a,&b,&c);
    if (a>b && a>c){
        printf("Biggest nums a=%d",a);
    }if(b>c && b>a){
        printf("Biggest nums b=%d",b);
    }if(c>b && c>a){ printf("Biggest nums c=%d",c);}
    return 0;
}