import sys
input = sys.stdin.readline
import heapq


N = int(input())
M = int(input())

cities = [[] for _ in range(N)]
D = [float('inf')] * N

for _ in range(M):

    s, e, c = map(int, input().split())
    cities[s-1].append((e-1, c))

start, end = map(int, input().split())
start, end = start - 1, end - 1


heap = []
heapq.heappush(heap, (0, start))
D[start] = 0

while heap:

    d, now = heapq.heappop(heap)  # 최소값

    if D[now] < d:
        continue

    for v, w in cities[now]:  # v : 연결된 정점, w : 비용

        cost = d + w
        if cost < D[v]:
            D[v] = cost
            heapq.heappush(heap, (cost, v))


print(D[end])



