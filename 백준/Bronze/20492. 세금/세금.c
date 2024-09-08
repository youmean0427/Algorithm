#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    int x;
    scanf("%d", &x);

    int y;
    int z;

    y = x - 0.22 * x;
    z = x - 0.22 * (x - 0.8*x);
    printf("%d %d", y, z);
}