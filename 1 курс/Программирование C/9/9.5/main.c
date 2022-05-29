#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define n 8

void fill(int *array) {
    for (int i = 0; i < n; i++) {
        array[i] = rand() % 200 - 100;
    }
}


int sum(int *arr, int num) {
    if (num == 0)
        return 0;
    else
        return sum(arr, num - 1) + arr[num - 1];
}

int main() {
    int a[n];
    srand(time(NULL));
    fill(a);
    printf("Array A:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("\n%d - sum\n", sum(a, n));
    return 0;
}
