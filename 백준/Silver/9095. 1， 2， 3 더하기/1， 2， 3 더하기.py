import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    table = [0, 1, 2, 4, 7]

    for i in range(5, N+1):

        cnt = table[i-1] + table[i-2] + table[i-3]
        table.append(cnt)

    print(table[N])