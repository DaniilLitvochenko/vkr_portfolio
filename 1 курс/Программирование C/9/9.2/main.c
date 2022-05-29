#include <stdio.h>
#include <stdlib.h>

int fib(int a) {
    if ((a == 1) || (a == 2)) {
        return 1;
    }
    return fib(a - 1) + fib(a - 2);
}

int main() {
    int a;
    printf("Enter num: \n");
    scanf_s("%d", &a);
    for (int i = 1; i <= a; i++) {
        printf("%d ", fib(i));
    }
    return 0;
}
