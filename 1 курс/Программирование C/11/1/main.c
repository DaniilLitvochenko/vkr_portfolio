#include <stdio.h>

typedef struct ctruct
{
    int (*functia)();
}strct;

void vivod()
{
    printf("TEST\n");
}

int main(){
    strct s;
    s.functia = &vivod;
    s.functia();
    return 0;
}
