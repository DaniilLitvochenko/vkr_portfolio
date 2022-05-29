#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define n 2
#define m 4

int main() {
    int a[n][m]={{1,2,1,3},{4,-1,5,-1}}, tr[m][n],res1[n][n]={{0,0},{0,0}},res2[m][m]={{0,0},{0,0},{0,0},{0,0}};

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            tr[i][j]=a[j][i];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < m; k++) {
                res1[i][j]+=a[i][k]*tr[k][j];
            }
        }
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            for (int k = 0; k < n; k++) {
                res2[i][j]+=tr[i][k]*a[k][j];
            }
        }
    }


    for (int i = 0; i < n; i++) {
        printf("\n");
        for (int j = 0; j < n; j++) {
            printf("%d ",res1[i][j]);
        }
    }


    for (int i = 0; i < m; i++) {
        printf("\n");
        for (int j = 0; j < m; j++) {
            printf("%d ",res2[i][j]);
        }
    }

    return 0;
}