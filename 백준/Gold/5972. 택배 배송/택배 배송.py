import sys, heapq
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    arr[A].append((C, B))
    arr[B].append((C, A))

def djik(start):

    heap = []
    heapq.heappush(heap, (0, start))
    D = [float('inf')] * (N+1)
    while heap:

        cost, node = heapq.heappop(heap)

        if cost > D[node]:
            continue

        for n_cost, n_node in arr[node]:
            if D[n_node] > cost + n_cost:
                D[n_node] = cost + n_cost
                heapq.heappush(heap, (cost+n_cost, n_node))

    return D

ans = djik(1)
print(ans[N])