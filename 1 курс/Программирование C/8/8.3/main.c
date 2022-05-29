#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

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

float arrgeom(float *arr, int count){
    float geom=1;
    int ind=0;
    for (int i = 0; i < count; i++) {
        if(arr[i]>0){geom*=arr[i]; ind+=1;}
    }
    geom=powf(geom,1.0/ind);
    return geom;
}

int main() {
    float a[n], v[m], c[k];
    srand(time(NULL));
    arrfill(a, n);
    printf("Array A geom=%.2f\n",arrgeom(a,n));
    printf("\n");
    arrfill(v, m);
    printf("Array V geom=%.2f\n",arrgeom(v,m));
    printf("\n");
    arrfill(c, k);
    printf("Array C geom=%.2f\n",arrgeom(c,k));
    printf("\n");
    return 0;
}