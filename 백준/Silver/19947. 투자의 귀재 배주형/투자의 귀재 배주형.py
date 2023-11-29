import sys
import math
input = sys.stdin.readline


def DFS(n, sm):
    global ans

    if n == Y:
        ans = max(ans, sm)
        return
    elif n > Y:
        return

    DFS(n+1, math.trunc(sm+sm*0.05))
    DFS(n+3, math.trunc(sm+sm*0.2))
    DFS(n+5, math.trunc(sm+sm*0.35))

ans = 0
H, Y = map(int, input().split())
DFS(0, H)
print(ans)