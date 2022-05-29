#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define n 2
#define m 2

int main() {
    int a[n][m]={{1,2},{3,0}}, b[n][m],kor[n][m]={{0},{0}},c[n][m]={{1,0},{0,1}};

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                kor[i][j]+=a[i][k]*a[k][j];
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            b[i][j]=-2*kor[i][j]+5*a[i][j]+9*c[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        printf("\n");
        for (int j = 0; j < m; j++) {
            printf("%d ",b[i][j]);
        }
    }
    return 0;
}