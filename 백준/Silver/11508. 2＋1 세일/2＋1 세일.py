import sys
input = sys.stdin.readline


N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

cost = 0
for k in range(0, N, 3):
    if N-k < 2:
        cost += sum(arr[k:])
        break
    else:
        cost += sum(arr[k:k+2])
print(cost)