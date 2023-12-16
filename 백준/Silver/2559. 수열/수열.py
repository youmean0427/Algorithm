import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(x) for x in input().split()]
result = -float('inf')

for x in range(1, N):
    arr[x] += arr[x-1]


for y in range(K-1, N):
    if y-K == -1:
        z = arr[y]
    else:
        z = arr[y] - arr[y-K]
    result = max(result, z)

if N == K:
    result = arr[K-1]

print(result)