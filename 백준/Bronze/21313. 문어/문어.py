import sys
input = sys.stdin.readline

N = int(input())

legs = [[0] * 8 for _ in range(N)]
octo = 0
s = []

while octo < N:
    if octo == N-1:
        for i in range(8):
            if legs[octo][i] == 0 and legs[0][i] == 0:
                legs[octo][i] = 1
                s.append(i + 1)
                break

    else:
        for i in range(8):
            if legs[octo][i] == 0:
                legs[octo][i] = 1
                legs[octo+1][i] = 1
                s.append(i+1)
                break

    octo += 1

print(*s)