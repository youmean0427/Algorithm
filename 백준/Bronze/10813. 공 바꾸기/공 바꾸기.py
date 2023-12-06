import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(x) for x in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a], arr[b] = arr[b], arr[a]

print(*arr[1:])