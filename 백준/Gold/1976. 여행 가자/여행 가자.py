import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

p = [int(i) for i in range(N+1)]

for city in range(1, N+1):
    arr = [int(i) for i in input().split()]

    for i, x in enumerate(arr):
        if x == 1:
            union(city, i+1)

plan = [int(i) for i in input().split()]
check = find_set(plan[0])
ans = 'YES'
for i in plan:
    if find_set(i) != check:
        ans = 'NO'
        break
print(ans)