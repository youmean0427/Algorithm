import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())
arr = []
for _ in range(E):
    A, B, C = map(int, input().split())
    arr.append((A, B, C))

p = [i for i in range(V+1)]

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(a, b, c):
    global result
    if find_set(b) != find_set(a):
        p[find_set(b)] = find_set(a)
        result += c

result = 0
arr.sort(key=lambda x: x[2])

for a, b, c, in arr:
    union(a, b, c)

print(result)
