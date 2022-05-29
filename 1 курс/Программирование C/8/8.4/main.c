#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define n 3

void printarr(int arr[][n]){
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
}


int main() {
    int s[n][n]={1,2,3,4,5,6,7,8,9}, k[n][n]={-1,2,-3,-4,-5,-6,-7,-8,9};
    printf("Array S:\n");
    printarr(s);
    printf("Array K:\n");
    printarr(k);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
                if (s[i][j] == k[i][j]) {
                    printf("%d \n", k[i][j]);
            }
        }
    }
    return 0;
}