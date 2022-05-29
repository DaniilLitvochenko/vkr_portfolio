#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define n 5

int main() {
    int arr[n],narr[n]={0};
    for (int i = 0; i < n; i++) {
        printf("Enter number %d\n",i);
        scanf_s("%d",&arr[i]);
    }
    for (int i = 0; i < n; i++) {
        narr[i]=arr[n-i-1];
    }
    for (int i = 0; i < n; i++) {
        printf("A[%d]=%d\n",i,narr[i]);
    }
    return 0;
}