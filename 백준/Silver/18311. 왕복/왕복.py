import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(x) for x in input().split()]
sum_arr = [0] + arr + arr[::-1]

index = []
for i in range(1, len(sum_arr)):
    sum_arr[i] += sum_arr[i-1]
    index.append(i)

index = index[:N] + index[N-1:0:-1] + [index[0]]

cnt = 0
for i in range(len(sum_arr)):
    if sum_arr[i] <= K:
        cnt = index[i]

print(cnt )