import sys, heapq
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, M, X = map(int, input().split())
arr = [[] for _ in range(N)]
arr2 = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a-1].append((b-1, c))
    arr2[b-1].append((a-1, c))

def djik(arr, party):

    heap = []
    heapq.heappush(heap, (0, party))
    visited = [float("inf")] * N
    visited[party] = 0

    while heap:

        cost, node = heapq.heappop(heap)

        if visited[node] < cost:
            continue

        for n, nc in arr[node]:
            next_cost = cost + nc
            if visited[n] > next_cost:
                visited[n] = next_cost
                heapq.heappush(heap, (next_cost, n))

    return visited

ans = 0
go = djik(arr, X-1)
back = djik(arr2, X-1)

for i in range(N):
    ans = max(ans, go[i] + back[i])

print(ans)