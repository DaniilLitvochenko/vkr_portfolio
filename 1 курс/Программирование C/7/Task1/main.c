#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define n 5

int main() {
    int arr[n];
    for (int i = 0; i < n; i++) {
        printf("Enter number %d\n",i);
        scanf_s("%d",&arr[i]);
    }
    for (int i = 0; i < n; i++) {
        arr[i]*=arr[i];
    }
    for (int i = 0; i < n; i++) {
        printf("A[%d]=%d\n",i,arr[i]);
    }
    return 0;
}