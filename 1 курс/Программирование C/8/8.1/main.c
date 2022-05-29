#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define n 6
#define m 8
#define k 7

void arrfill(float *arr, int count){
    printf("Array: \n");
    for (int i = 0; i < count; i++) {
        arr[i] = (float)(rand() % (10000 - -10000 + 1)) / 100 - 100;
        printf("Arr[%d]=%.2f\n", i, arr[i]);
    }
}

float arrsum(float *arr, int count){
    float sum=0;
    for (int i = 0; i < count; i++) {
        if(arr[i]>0)sum+=arr[i];
    }
    return sum;
}

int main() {
    float a[n], a1[m], c[k];
    srand(time(NULL));
    arrfill(a, n);
    printf("Array A sum=%.2f\n",arrsum(a,n));
    arrfill(a1, m);
    printf("Array A1 sum=%.2f\n",arrsum(a1,m));
    arrfill(c, k);
    printf("Array C sum=%.2f\n",arrsum(c,k));
    printf("All array sum=%.2f\n",arrsum(a,n)+arrsum(a1,m)+arrsum(c,k));
    return 0;
}