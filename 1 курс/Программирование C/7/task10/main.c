#include<stdio.h>
#include<stdlib.h>
#include <math.h>

#define n 2

int main() {
    float a[n][n], sum = 0;


    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            scanf_s("%f",&a[i][j]);
    }

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
        {

            sum += a[i][j];
            if (j+1 == n)
            {
                a[i][0] = sum/n;
                sum = 0;
            }
        }
    printf("Result: \n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            printf("%.2f ", a[i][j]);
        printf("\n");
    }

    return 0;
}
