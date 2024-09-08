#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long long power(int A, int x, int C)
{
    long long y;
    if (x == 0)
        return (1);
    else
    {
        y = power(A, x/2, C);
        if (x % 2 == 0)
            return y % C * y % C % C;
        else
            return y % C * y % C * A % C;
    }

}

int main(void)
{
    int a;
    int b;
    int c;

    scanf("%d %d %d", &a, &b, &c);
    printf("%lld", power(a, b, c));
    return (0);
}