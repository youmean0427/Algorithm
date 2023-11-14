import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())

arr = []

for i in range(1, K+1):
    x = str(N * i)[::-1]
    arr.append(int(x))

print(max(arr))