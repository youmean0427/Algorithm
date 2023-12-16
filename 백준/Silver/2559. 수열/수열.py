import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(x) for x in input().split()]
result = sum(arr[:K])

for x in range(1, N):
    arr[x] += arr[x-1]

for y in range(K, N):
    z = arr[y] - arr[y-K]
    result = max(result, z)

print(result)