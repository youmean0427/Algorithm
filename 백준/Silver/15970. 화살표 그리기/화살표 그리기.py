import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr = sorted(arr, key = lambda x: (x[1], x[0]))

cnt = [float('inf')] * len(arr)
for i in range(1, len(arr)):
    if arr[i][1] == arr[i-1][1]:
        cnt[i-1] = min(cnt[i-1], arr[i][0] - arr[i-1][0])

for i in range(len(arr)-1, 0, -1):
    if arr[i][1] == arr[i-1][1]:
        cnt[i] = min(cnt[i], arr[i][0] - arr[i-1][0])

print(sum(cnt))