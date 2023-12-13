T = int(input())

for _ in range(T):

    N, M = map(int, input().split())

    m = M
    n = N

    for i in range(1, N):
        m *= M - i
        n *= i

    print((m // n))