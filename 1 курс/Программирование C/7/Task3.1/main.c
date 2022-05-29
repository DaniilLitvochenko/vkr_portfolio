#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define n 5

int main() {
    int arr[n],temp;
    for (int i = 0; i < n; i++) {
        printf("Enter number %d\n",i);
        scanf_s("%d",&arr[i]);
    }

    for (int i = n-1; i >0; i--) {
        for (int j = n-1; j >0; j--) {
            if(arr[j]<arr[j-1]){
                temp=arr[j-1];
                arr[j-1]=arr[j];
                arr[j]=temp;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        printf("A[%d]=%d\n",i,arr[i]);
    }
    return 0;
}