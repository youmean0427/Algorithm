import sys
from collections import deque
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

def bfs(A, B):
    q = deque([A])
    visited = ["" for _ in range(10000)]
    visited[A] = "X"
    while q:

        x = q.popleft()

        if x == B:
            print(visited[x][1:])
            return

        # D
        D = x * 2
        if D > 9999:
            D = D % 10000

        if D == B:
            print(visited[x][1:] + 'D')
            return

        if visited[D] == "":
            visited[D] = visited[x] + 'D'
            q.append(D)

        # S

        S = x - 1
        if x == 0:
            S = 9999

        if S == B:
            print(visited[x][1:] + 'S')
            return

        if visited[S] == "":
            visited[S] = visited[x] + 'S'
            q.append(S)

        # L
        L = (x % 1000) * 10 + x // 1000

        if L == B:
            print(visited[x][1:] + 'L')
            return

        if visited[L] == "":
            visited[L] += visited[x] + 'L'
            q.append(L)

        # R
        R = (x % 10) * 1000 + (x // 10)

        if R == B:
            print(visited[x][1:] + 'R')
            return

        if visited[R] == "":
            visited[R] = visited[x] + 'R'
            q.append(R)


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    # A : 초기값 / B : 최종값
    bfs(A, B)