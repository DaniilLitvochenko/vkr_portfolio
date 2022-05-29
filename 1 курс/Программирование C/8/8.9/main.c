#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <time.h>

void doublearray(int n, int m){
    int *a;
    a=(int*)malloc(n*m*sizeof(int));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            *(a+i*m+j)=rand()%200-100;
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%3d ",*(a+i*m+j));
        }
        printf("\n");
    }
    free(a);
}

int main() {
    int n, m;
    srand(time(NULL));
    printf("Enter count strok and stolbsov: \n");
    scanf_s("%d %d", &n, &m);
    doublearray(n,m);
    return 0;
}