#include <stdio.h>
#include <stdlib.h>

int main() {
    char* p1 = malloc(10);
    printf("p1:%x\n", p1);
    free(p1);

    char* p2 = malloc(10);
    printf("p2:%x\n", p2);
    free(p2);
}