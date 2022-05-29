#include <stdio.h>

int main() {
    int a,b,sum;
    printf("Enter interval: \n");
    scanf_s("%d %d",&a,&b);
    sum=0;
    for (int i = a; i <= b; i++) {
        for (int j =a ; j < i; j++) {
            if(i%j==0){sum+=j;}
        }
        if(i==sum){printf("%d ",i);}
        sum=0;
    }
    return 0;
}