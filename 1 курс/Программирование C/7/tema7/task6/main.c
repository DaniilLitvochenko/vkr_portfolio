#include <stdio.h>

int main() {
    int a, b, c;
    printf("Enter a,b,c:\n");
    scanf_s("%d %d %d",&a,&b,&c);
    if(a<b+c && c<b+a && c<b+a) {
        printf("Exist\n");
        {
            if (a * a == c * c + b * b | b * b == c * c + a * a | c * c == b * b + a * a) {
                printf("Pryamougolny");
            }
        }
    }else{printf("No");}
    return 0;
}