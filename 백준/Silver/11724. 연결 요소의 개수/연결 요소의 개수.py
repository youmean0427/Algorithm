import sys, heapq
# sys.stdin = open('EX.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list([0] * (N+1) for _ in range(N+1))
visited = [0] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    arr[x][y], arr[y][x] = 1, 1

count = 0
for i in range(1, N+1):
    if visited[i] == 0:
        q = [i]

        while q:
            # print(q ,visited)
            point = q.pop()

            if visited[point] == 0:
                visited[point] = 1

            for j in range(1, N+1):
                if arr[point][j] == 1:
                    if visited[j] == 0:
                        visited[j] = 1
                        q.append(j)

        count += 1
    else:
        pass

print(count)