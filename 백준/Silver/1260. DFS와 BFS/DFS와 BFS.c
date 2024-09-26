#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void dfs(int **arr, int start, int n, int m)
{
    int *stack;
    int top;
    int *visited;
    int pop;

    top = 0;
    visited = (int *)malloc(sizeof(int) * (n+1));
    for (int j = 0; j <= n; j++)
        visited[j] = 0;
    stack = (int *)malloc(sizeof(int) * (n * m));
    for (int j = 0; j < n * m; j++)
        stack[j] = 0;
    stack[0] = start;
 
    while (top >= 0)
    {
        pop = stack[top];
        top--;
        if (visited[pop] == 0)
              printf("%d ", pop);
        visited[pop] = 1;
        for (int i = n; i > 0; i--)
        {
            if (arr[pop][i] == 1)
            {
                if (visited[i] == 0)
                {
                    top++;
                    stack[top] = i;
                }
            }
        }
    }
}

void bfs(int **arr, int start, int n, int m)
{
    int *queue;
    int *visited;

    visited = (int *)malloc(sizeof(int) * (n+1));
    for (int j = 0; j <= n; j++)
        visited[j] = 0;
    queue = (int *)malloc(sizeof(int) * (n * m));
    for (int j = 0; j < n * m; j++)
        queue[j] = 0;
    queue[0] = start;
    visited[start] = 1;

    int front;
    int rear;
    int pop;

    front = -1;
    rear = 0;
    while (front < rear)
    {
        pop = queue[++front];
        printf("%d ", pop);
        for (int i = 0; i <= n; i++)
        {
            if (arr[pop][i] == 1)
            {
                if (visited[i] == 0)
                {
                    visited[i] = 1;
                    queue[++rear] = i;
                }
            }
        }
    }
}

int main(void)
{
    int n, m, v;

    scanf("%d %d %d", &n, &m, &v);
    
    int **arr;
    
    arr = (int **)malloc(sizeof(int *) * (n+1));
    for (int i = 0; i < n+1; i++) {
        arr[i] = (int *)malloc(sizeof(int) * (n+1));
        for (int j = 0; j < n+1; j++)
        {
            arr[i][j] = 0;
        }
    }

    for (int i = 0; i < m; i++)
    {
        int a;
        int b;
        scanf("%d %d", &a, &b);
        arr[a][b] = 1;
        arr[b][a] = 1;
    }
    dfs(arr, v, n, m);
    printf("\n");
    bfs(arr, v, n, m);
}