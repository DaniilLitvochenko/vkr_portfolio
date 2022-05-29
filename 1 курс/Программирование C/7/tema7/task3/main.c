#include <stdio.h>

int main() {
    int a;
    printf("Enter num: \n");
    scanf_s("%d", &a);
    for (int i = 1; i < a+2; i++) {
        printf("%d ",i);
    }
    return 0;
}