#include <stdio.h>
#include <stdlib.h>

typedef struct spisok {
    int value;
    struct spisok *next;
    struct spisok *prev;
}spisok;

spisok* create(int n) {
    spisok* begin = malloc(sizeof(spisok));
    int a;
    printf_s("Enter num: \n");
    scanf_s("%d",&a);
    begin->value = a;
    begin->prev = NULL;
    spisok *onStruct, *onStructNext;
    onStruct = begin;
    for (int i = 1; i < n; i++) {
        onStructNext = malloc(sizeof(spisok));
        printf_s("Enter next num: \n");
        scanf_s("%d",&a);
        onStructNext->value = a;
        onStruct->next = onStructNext;
        onStructNext->prev = onStruct;
        onStruct = onStructNext;
    }
    onStruct->next = NULL;
    return begin;
}

void print(spisok *begin) {
    spisok *onStruct = begin;
    spisok *onStructPosl;
    while (onStruct != NULL) {
        printf("%d ", onStruct->value);
        onStructPosl = onStruct;
        onStruct = onStruct->next;
    }
    printf("\n");
    while (onStructPosl != NULL) {
        printf("%d ", onStructPosl->value);
        onStructPosl = onStructPosl->prev;
    }
}

void freespisok(spisok *begin) {
    spisok *onStructNext = begin->next;
    if (onStructNext != NULL) {
        freespisok(onStructNext);
    }
    free(begin);
}

int main() {
    int n;
    printf_s("Enter lenght: \n");
    scanf_s("%d", &n);
    spisok *list = create(n);
    print(list);
    freespisok(list);
    return 0;
}
