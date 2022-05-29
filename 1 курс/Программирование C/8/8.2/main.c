#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define n 8

void arrfill(int *arr){
    printf("Array: \n");
    for (int i = 0; i < n; i++) {
        arr[i] =rand()%200-100;
        printf("Arr[%d]=%d\n", i, arr[i]);
    }
}

int arrmax(int *arr){
    float max=arr[0];
    for (int i = 0; i < n; i++) {
        if(arr[i]>max)max=arr[i];
    }
    return max;
}

int main() {
    int a[n], b[n];
    srand(time(NULL));
    arrfill(a);
    printf("Max A=%d\n",arrmax(a));
    arrfill(b);
    printf("Max B=%d\n",arrmax(b));
    printf("Summ max: %d",arrmax(a)+arrmax(b));
    return 0;
}