import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr = []
for _ in range(M):
    a, b, c = map(int, input().split())
    arr.append((a, b, c))

D = [float('inf')] * (N+1)

def bellman_ford(start):
    D[start] = 0

    for i in range(N):
        for j in range(M):
            now = arr[j][0]
            next = arr[j][1]
            cost = arr[j][2]

            if D[now] != float('inf') and D[next] > D[now] + cost:
                D[next] = D[now] + cost

                if i == N-1:
                    # Negative Cycle exists
                    return False
    return True

if bellman_ford(1):
    for i in D[2:]:
        if i == float('inf'):
            print(-1)
        else:
            print(i)

else:
    print(-1)