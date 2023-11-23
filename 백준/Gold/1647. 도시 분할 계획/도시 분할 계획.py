import sys
import heapq
input = sys.stdin.readline

def prim(x):
    heap = []
    heapq.heappush(heap, (0, x))
    result = 0
    while heap:
        c, y = heapq.heappop(heap)

        if visited[y] == 0:
            visited[y] = 1
            key[y] = c
            result += c
            for k in arr[y]:
                if visited[k[1]] == 0:
                    heapq.heappush(heap, (k[0], k[1]))

    return result

N, M = map(int, input().split())
arr = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
key = [0] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    arr[b].append((c, a))
    arr[a].append((c, b))

result = prim(1)
x = result
for i in range(1, N+1):
    x = min(x, result - key[i])

print(x)

