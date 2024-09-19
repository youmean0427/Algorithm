#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void    arr_init(char *arr)
{
    for (int i = 0; i < 1000; i++)
        arr[i] = 0;
}

int main(void)
{
    int n;
    char arr[1001];
    
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {   
        arr_init(arr);
        scanf("%s", arr);

        int idx;
        int now;
        int cnt;
        idx = 1;
        cnt = 1;
        now = arr[0];

        while (arr[idx])
        {
            if (now == arr[idx])
                cnt++;
            else
            {
                printf("%d%c", cnt, now);
                now = arr[idx];
                cnt = 1;
            }
            idx++;
        }
        printf("%d%c\n", cnt, now);
    }
}