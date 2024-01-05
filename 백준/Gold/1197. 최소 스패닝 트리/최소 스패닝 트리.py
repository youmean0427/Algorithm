import sys
input = sys.stdin.readline

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y, z):
    global result
    if find_set(x) != find_set(y):
        p[find_set(y)] = find_set(x)
        result += z

V, E = map(int, input().split())
arr = []
p = [int(i) for i in range(0, V+1)]
result = 0
for _ in range(E):
    a, b, c = map(int, input().split())
    arr.append([a, b, c])

arr.sort(key=lambda x:x[2])
for a, b, c in arr:
    union(a, b, c)

print(result)

