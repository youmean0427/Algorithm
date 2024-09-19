#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(void)
{
    int b;
    int d;
    int c;
    int t;
    int check = 0;

    scanf("%d %d %d %d", &b, &d, &c, &t);

    for (int i = 0; i <= t; i++)
    {
        for (int j = 0; j <= t; j++)
        {
            for (int k = 0; k <= t; k++)
            {
                if (b * i + d * j + c * k == t)
                {   
                    check = 1;
                    printf("%d %d %d\n", i, j, k);
                }
            }
        }
    }
    if (check == 0)
        printf("impossible");
}