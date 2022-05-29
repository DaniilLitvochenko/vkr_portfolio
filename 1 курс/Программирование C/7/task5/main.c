#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define n 3
#define m 3

int main() {
    int a[n][m];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf_s("%d",&a[i][j]);
        }
    }

    for (int i = 0; i < n; i++) {
        printf("\n");
        for (int j = 0; j < m; j++) {
            printf("%d ",a[i][j]);
        }
    }
    return 0;
}