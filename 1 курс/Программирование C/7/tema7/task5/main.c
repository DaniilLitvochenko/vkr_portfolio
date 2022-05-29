#include <stdio.h>
#include <stdlib.h>

int main() {
    for (int i = 10; i <= 99; i++) {
        if(i%(i%10+(i/10)%10)==0){printf("%d ",i);}
    }

    return 0;
}