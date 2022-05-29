#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <malloc.h>

int main() {
    int **a, n,m, k;

    printf("Enter count strok and stolbsov: \n");
    scanf_s("%d %d", &n, &m);

    a=(int**)malloc(n* sizeof(int*));

    for (int i = 0; i < n; i++) {
        a[i]=(int*)malloc(n* sizeof(int));
        for (int j = 0; j < m; j++) {
            a[i][j]=rand()%10;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }
    printf("Enter stroka to delete: \n");
    scanf_s("%d",&k);
    for (int i = 0; i < n; i++) {
        a[k-1][i]=0;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < n; i++) free(a[i]);
    free(a);
    return 0;
}