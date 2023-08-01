import sys
# sys.stdin = open('EX.txt', 'r')
input = sys.stdin.readline

N = int(input())
M = int(input())

cpu = list([0 for _ in range(N+1)] for _ in range(N+1))

for _ in range(M):
    a, b = map(int, input().split())

    cpu[a][b] = 1
    cpu[b][a] = 1

visited = [0] * (N+1)
visited[1] = 1

q = [1]
while q:
    if q:
        start = q.pop()

    if visited[start] == 0:
        visited[start] = 1

    for i in range(N+1):
        if cpu[start][i] == 1:
            if visited[i] == 0:
                q.append(i)

print(visited.count(1)-1)