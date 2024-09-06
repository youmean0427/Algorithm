#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int     can_go(int *arr, int x)
{
        for (int i = 0; i < x; i++)
        {
                
                if (arr[i] == arr[x] || abs(arr[i] - arr[x]) == abs(i - x))
                {
                        return (0);
                }
        }
        return (1);

}

void     dfs(int *arr, int x, int n, int *ans)
{
        if (x == n)
        {
                (*ans)++;
                return ;
        }
        for (int i = 0; i < n; i++)
        {
                arr[x] = i; 

                if (can_go(arr, x))
                {
                        dfs(arr, x+1, n, ans);
                }
        }

}

int     main(void)
{       
        int     n;
        int     *arr;
        int     ans;

        scanf("%d", &n);
        ans = 0;
        arr = (int *)malloc(sizeof (int) * n);
        dfs(arr, 0, n, &ans);
        printf("%d", ans);
        free(arr);
}