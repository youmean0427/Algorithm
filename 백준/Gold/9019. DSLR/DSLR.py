import sys
from collections import deque
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

def bfs(A, B):
    q = deque([[A, ""]])
    visited = [0] * 10001
    visited[A] = 1
    while q:

        x, y = q.popleft()

        if x == B:
            print(y)
            return

        # D
        D = x * 2
        if D > 9999:
            D = D % 10000

        if D == B:
            print(y+"D")
            return

        if visited[D] == 0:
            visited[D] = 1
            q.append([D, y+"D"])

        # S

        S = x - 1
        if x == 0:
            S = 9999

        if S == B:
            print(y + "S")
            return

        if visited[S] == 0:
            visited[S] = 1
            q.append([S, y + "S"])

        # L
        L = (x % 1000) * 10 + x // 1000

        if L == B:
            print(y + "L")
            return

        if visited[L] == 0:
            visited[L] = 1
            q.append([L, y + "L"])

        # R
        R = (x % 10) * 1000 + (x // 10)

        if R == B:
            print(y + "R")
            return

        if visited[R] == 0:
            visited[R] = 1
            q.append([R, y + "R"])


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    # A : 초기값 / B : 최종값
    bfs(A, B)