#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define n 5

int main() {
    int arr[n],temp1, j;
    for (int i = 0; i < n; i++) {
        printf("Enter number %d\n",i);
        scanf_s("%d",&arr[i]);
    }

    for (int i=0; i < n; i++)
    {
        temp1 = arr[i];
        for (j=i-1; j>=0 && arr[j]>temp1; j--){
            arr[j+1] = arr[j];
        }
        arr[j+1] = temp1;
    }

    for (int i = 0; i < n; i++) {
        printf("A[%d]=%d\n",i,arr[i]);
    }
    return 0;
}