import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    T, S = map(int, input().split())
    arr.append((T, S))

arr = sorted(arr, key = lambda x : x[1])
T = arr[-1][1] - arr[-1][0]

for i in range(N-2, -1, -1):
    if T > arr[i][1]:
        T = arr[i][1] - arr[i][0]
    else:
        T = T - arr[i][0]

if T - 1 < 0:
    print(-1)
else:
    print(T)