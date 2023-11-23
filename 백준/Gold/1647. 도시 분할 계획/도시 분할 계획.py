import sys
import heapq
input = sys.stdin.readline

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y, c):
    global result
    if find_set(x) != find_set(y):
        p[find_set(y)] = find_set(x)
        result += z
        key[y] = z

N, M = map(int, input().split())

arr = []
key = [0] * (N+1)

p = [i for i in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    arr.append([a, b, c])

arr.sort(key = lambda x:x[2])

cnt = 0
result = 0
while cnt < M:
    x, y, z = arr[cnt][0], arr[cnt][1], arr[cnt][2]
    union(x, y, z)
    cnt += 1

x = result
for i in range(1, N+1):
    x = min(x, result - key[i])

print(x)
