#include <stdio.h>
#include <stdlib.h>

int k(int a) {
    if (a < 10)
        return 1;
    else
        return k(a / 10) + 1;
}

int main() {
    int a;
    printf("Enter num\n");
    scanf_s("%d", &a);
    printf("In num %d %d nums\n", a, k(a));
    return 0;
}
