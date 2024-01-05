import sys
input = sys.stdin.readline
import heapq

def prim(x):

    heap = []
    key[x] = 0
    heapq.heappush(heap, [0, x])

    while heap:
        w, n = heapq.heappop(heap)

        if visited[n] == 0:
            visited[n] = 1
            for i in arr[n]:
                if visited[i[1]] == 0:
                    key[i[1]] = i[0]
                    heapq.heappush(heap, (i[0], i[1]))

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    key = [0] * (N+1)
    visited = [0] * (N+1)
    arr = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a].append([1, b])
        arr[b].append([1, a])

    prim(1)
    print(sum(key))