#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define n 2
#define m 3

int main() {
    int a[n][m]={{1,2,3},{4,5,6}}, tr[m][n];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            tr[i][j]=a[j][i];
        }
    }

    for (int i = 0; i < m; i++) {
        printf("\n");
        for (int j = 0; j < n; j++) {
            printf("%d ",tr[i][j]);
        }
    }
    return 0;
}