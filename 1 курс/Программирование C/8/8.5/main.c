#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define n 6
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

int sum(int arr[n][m]){
    int nsum=0, sum=0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (arr[i][j]>0)nsum+=arr[i][j];
        }
        if(nsum>sum)sum=nsum;
        nsum=0;
    }
    return sum;
}


int main() {
    int d[n][m];
    srand(time(NULL));
    printf("Array D:\n");
    arrfill(d);
    printarr(d);
    printf("%d",sum(d));
    return 0;
}
