#include <stdio.h>
#include <stdlib.h>

int main(void)
{
        int     n;
        char    c;
        char    s[6];
        int     arr[26];
        int     total;
        int     cnt;

        for (int i = 0; i <= 25; i++)
                arr[i] = 0;
        total = 0;
        cnt = 0;
        while (1)
        {
                scanf("%d", &n);
                if (n == -1)
                        break;
                scanf(" %c %s", &c, s);
                if (s[0] == 'w')
                        arr[c - 65] += 1;
                else
                {
                        total = total + n + arr[c - 65] * 20;
                        cnt += 1;
                }
        }
        printf("%d %d", cnt, total);
}