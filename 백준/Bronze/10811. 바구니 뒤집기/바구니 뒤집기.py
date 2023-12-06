import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(x) for x in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a:b+1] = arr[b:a-1:-1]

print(*arr[1:])