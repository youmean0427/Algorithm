import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_set(x):
    if arr[x] != x:
        arr[x] = find_set(arr[x])
    return arr[x]

def union(x, y):
    arr[find_set(y)] = find_set(x)

def check(x, y):
    if arr[find_set(x)] == arr[find_set(y)]:
        return "YES"
    else:
        return "NO"

n, m = map(int, input().split())
arr = [x for x in range(n+1)]
result = ''

for _ in range(m):
    x, a, b = map(int, input().split())

    if x == 0:
        union(a, b)
    else:
        result = check(a, b)
        print(result)