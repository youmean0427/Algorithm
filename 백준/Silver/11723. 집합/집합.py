from collections import deque
import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):

    N = list(input().split())

    if N[0] == 'add':
        S.add(int(N[1]))

    if N[0] == 'remove':
        S.discard(int(N[1]))

    if N[0] == 'check':
        if int(N[1]) in S:
            print(1)
        else:
            print(0)

    if N[0] == 'toggle':
        if int(N[1]) in S:
            S.discard(int(N[1]))
        else:
            S.add(int(N[1]))

    if N[0] == 'all':
        S = set([i for i in range(1, 21)])
    if N[0] == 'empty':
        S = set()