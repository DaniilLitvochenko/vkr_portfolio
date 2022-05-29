#include <stdio.h>
#include <stdlib.h>

int main() {
    int a;
    printf("Enter num: \n");
    scanf_s("%d", &a);
    switch(a){
        case 1:
            printf("Lol chto, odnougolnik?");
            break;
        case 2:
            printf("Dvuugolnik, da?");
            break;
        case 3:
            printf("Treugolnik");
            break;
        case 4:
            printf("Chetirehugolnik");
            break;
        case 5:
            printf("Pyatiugolnik");
            break;
        case 6:
            printf("Mnogoulnik");
            break;
        default:
            printf("Oche mnogoulnik");
            break;
    }
    return 0;
}