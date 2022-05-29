#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <malloc.h>

int main() {
    int **a, **b, **c, n,m;

    printf("Enter count strok and stolbsov: \n");
    scanf_s("%d %d", &n, &m);

    a=(int**)malloc(n* sizeof(int*));
    for (int i = 0; i < n; i++) {
        a[i]=(int*)malloc(n* sizeof(int));
        for (int j = 0; j < m; j++) {
            a[i][j]=rand()%10;
        }
    }

    printf("Matrix M\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }

    b=(int**)malloc(n* sizeof(int*));
    for (int i = 0; i < n; i++) {
        b[i]=(int*)malloc(1* sizeof(int));
        for (int j = 0; j < 1; j++) {
            b[i][j]=rand()%10;
        }
    }

    printf("Vector a:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 1; j++) {
            printf("%d ",b[i][j]);
        }
        printf("\n");
    }


    c=(int**)malloc(n* sizeof(int*));
    for (int i = 0; i < n; i++) {
        c[i]=(int*)malloc(1* sizeof(int));
        for (int j = 0; j < 1; j++) {
            c[i][j]=0;
            for (int k = 0; k < n; k++) {
                c[i][j]=a[i][j]*b[i][j];
            }
        }
    }


    printf("Vector b: \n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 1; j++) {
            printf("%d ",c[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < n; i++) {
        free(a[i]);
        free(b[i]);
        free(c[i]);
    }

    free(a);
    free(b);
    free(c);

    return 0;
}