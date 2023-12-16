import sys, copy
input = sys.stdin.readline

S = input().rstrip()
N = int(input())
arr = [{S[0] : 1} for _ in range(len(S)+1)]
arr[-1] = {}

for i in range(1, len(S)):
    arr[i] = arr[i-1].copy()
    if S[i] in arr[i]:
        arr[i][S[i]] += 1
    else:
        arr[i][S[i]] = 1

for _ in range(N):
    a, start, end = input().split()
    start = int(start)
    end = int(end)

    x = 0
    y = 0
    if a in arr[end]:
        x = arr[end][a]
    if a in arr[start-1]:
        y = arr[start-1][a]

    print(x - y)