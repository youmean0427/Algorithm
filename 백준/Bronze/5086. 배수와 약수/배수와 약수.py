import sys
input = sys.stdin.readline


while True:
    N, M = map(int, input().split())
    answer = "neither"
    if N == 0 and M == 0:
        break

    for i in range(1, M):
        if M % i == 0 and i == N:
            answer = "factor"
            break

    for i in range(N, 1, -1):
        if N % i == 0 and i == M:
            answer = "multiple"
            break

    print(answer)
