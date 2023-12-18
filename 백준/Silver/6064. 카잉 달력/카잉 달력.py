import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    cnt = -1
    for i in range(0, M*N+1, M):
        if ((i + x) - x) % M == 0 and ((i + x)-y) % N == 0:
            cnt = i+x
            break

    print(cnt)
