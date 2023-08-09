import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int,input().split()))

for i in range(1, N):
    num[i] += num[i-1]

for _ in range(M):
    start, end = map(int, input().split())
    if start == 1:
        print(num[end-1])
    else:
        print(num[end-1] - num[start-2])
