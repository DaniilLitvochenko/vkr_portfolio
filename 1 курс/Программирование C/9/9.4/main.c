#include <stdio.h>
#include <stdlib.h>

int c(int m, int n) {
    if (m == 0 || m == n)
        return 1;
    else
        return c(m, n - 1) + c(m - 1, n - 1);
}

int main() {
    int m, n;
    printf("Enter m and n: prim(0<=m<=n)\n");
    scanf_s("%d %d", &m, &n);
    printf("Result: %d\n", c(m, n));
    return 0;
}
