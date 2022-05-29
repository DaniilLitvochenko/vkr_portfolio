#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int prost(int a){
    int prostch=0;
    for (int i = 2; i < a; i++) {
        if(a%i==0)prostch=1;
    }
    return prostch;
}

int main() {
    int a=1;
    printf("Enter num: \n");
    while(a!=0){
        scanf_s("%d",&a);
        if(a==0){break;}
        if(prost(a)==0){
            printf("%d - prostoe\n", a);
        }else{
            printf("%d - ne prostoe...\n", a);
        }
        printf("Enter 0 to exit\n");
    }
    return 0;
}