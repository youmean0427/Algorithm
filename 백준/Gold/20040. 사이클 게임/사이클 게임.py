import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
p = [int(i) for i in range(n)]

def find_set (x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y, i):
    global cnt
    xp = find_set(x)
    yp = find_set(y)

    if xp == yp:
        cnt = i
        print(i+1)
        exit(0)
    elif xp < yp:
        p[yp] = xp
    else:
        p[xp] = yp

cnt = 0
for i in range(m):
    a, b = map(int, input().split())
    union(a, b, i)

print(cnt)