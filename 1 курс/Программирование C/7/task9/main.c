#include<stdio.h>
#include<stdlib.h>
#include <math.h>

#define n 2

int main() {
    int a[n][n] = { {1,-1},{-1,1} }, b[n][n] = { {2,0},{-3,1} }, c[n][n] = { {3,-1},{2,3} },res1[n][n] = { {0,0},{0,0} }, res2[n][n] = { {0,0},{0,0} }, res3[n][n] = { {0,0},{0,0} }, res4[n][n] = { {0,0},{0,0} };

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            a[i][j] = a[j][i];

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            for (int k = 0; k < n; k++)
                res1[i][j] += a[i][k] * b[k][j];

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            for (int k = 0; k < n; k++)
                res2[i][j] += res1[i][k] * c[k][j];

    printf("(AB)*C= :\n");

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            printf("%d ", res2[i][j]);
        printf("\n");
    }

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            for (int k = 0; k < 2; k++)
                res3[i][j] += b[i][k] * c[k][j];

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            for (int k = 0; k < 2; k++)
                res4[i][j] += a[i][k] * res3[k][j];
    printf("A*(BC):\n");

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            printf("%d ", res4[i][j]);
        printf("\n");
    }
    return 0;
}
