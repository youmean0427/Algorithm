import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    x = [int(x) for x in input().split()]
    arr.append(x)
visited = [[0] * n for _ in range(n)]
visited[0][0] = arr[0][0]
for i in range(0, len(arr)-1):
    for j in range(0, len(arr[i+1])-1):
        visited[i+1][j] = max(visited[i+1][j], visited[i][j] + arr[i+1][j])
        visited[i+1][j+1] = max(visited[i+1][j+1], visited[i][j] + arr[i+1][j+1])

print(max(visited[-1]))

