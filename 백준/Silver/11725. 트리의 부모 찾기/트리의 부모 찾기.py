import sys
input = sys.stdin.readline


def BFS(arr, start):

    visited = [0] * len(arr)
    visited[start] = 1

    queue = [start]

    while queue:

        x = queue.pop(0)

        for i in arr[x]:
            if visited[i] == 0:
                visited[i] = x
                queue.append(i)
    return visited

N = int(input())
arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

result = BFS(arr, 1)
for i in range(2, len(result)):
    print(result[i])
