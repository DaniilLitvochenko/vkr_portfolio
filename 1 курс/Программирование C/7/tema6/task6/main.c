#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <malloc.h>

int main() {
    int **a, n, m;

    printf("Enter count strok and stolbsov: \n");
    scanf_s("%d %d", &n, &m);

    a = (int **) malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++) {
        a[i] = (int *) malloc(n * sizeof(int));
        for (int j = 0; j < m; j++) {
            if((i+j)%2==0){a[i][j]=0;}else{a[i][j]=1;}
        }
    }

    printf("Matrix M\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }

    return 0;
}