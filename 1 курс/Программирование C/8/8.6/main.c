#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define n 3
#define m 5

void arrfill(int arr[n][m]){
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            arr[i][j]=rand()%100;
        }
    }

}

void printarr(int arr[n][m]){
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
}

void geom(int arr[n][m]){
    float geom;
    for (int i = 0; i < n; i++) {
        geom=1;
        for (int j = 0; j < m; j++) {
            geom*=arr[i][j];
        }
        geom=powf(geom, 1.0/m);
        printf("Geom %d string=%.2f\n",i,geom);
    }
}


int main() {
    int d[n][m];
    srand(time(NULL));
    printf("Array D:\n");
    arrfill(d);
    printarr(d);
    geom(d);
    return 0;
}
