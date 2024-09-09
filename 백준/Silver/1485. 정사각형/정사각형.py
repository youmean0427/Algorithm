import sys
input = sys.stdin.readline

def length(x, y, p, q):
    return (((p - x) ** 2 + (q - y) ** 2) ** (1/2))

t = int(input())
for _ in range(t):
    dot = []
    for _ in range(4):
        x, y = map(int, input().split())
        dot.append((x, y))
    dot.sort(key=lambda x: (x[0], x[1]))
    ans = 1
    line = length(dot[0][0], dot[0][1], dot[1][0], dot[1][1])
    if line != length(dot[3][0], dot[3][1], dot[1][0], dot[1][1]):
        ans = 0
    if line != length(dot[3][0], dot[3][1], dot[2][0], dot[2][1]):
        ans = 0
    if line != length(dot[0][0], dot[0][1], dot[2][0], dot[2][1]):
        ans = 0
    if length(dot[0][0], dot[0][1], dot[3][0], dot[3][1]) != length(dot[1][0], dot[1][1], dot[2][0], dot[2][1]):
        ans = 0
    print(ans)