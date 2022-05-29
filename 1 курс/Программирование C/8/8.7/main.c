#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define n 3
#define m 5

void arrfill(int arr[n][m]){
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            arr[i][j]=rand()%200-100;
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

void minstr(int arr[n][m]){
    int min;
    for (int i = 0; i < n; i++) {
        min=arr[i][0];
        for (int j = 0; j < m; j++) {
            if(min>arr[i][j])min=arr[i][j];
        }
        printf("Min %d string=%d\n", i, min);

    }
}


int main() {
    int d[n][m];
    srand(time(NULL));
    printf("Array D:\n");
    arrfill(d);
    printarr(d);
    minstr(d);
    return 0;
}
