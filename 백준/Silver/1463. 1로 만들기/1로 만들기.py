import sys
input = sys.stdin.readline

N = int(input())

table = [0, 0, 1, 1]
for i in range(4, N+1):
    case = []
    cnt = 0

    if i % 2 == 0:
        cnt += 1
        cnt += table[i // 2]
        case.append(cnt)
        cnt = 0

    if i % 3 == 0:
        cnt += 1
        cnt += table[i // 3]
        case.append(cnt)
        cnt = 0

    i -= 1
    cnt += 1
    cnt += table[i]
    case.append(cnt)

    table.append(min(case))

print(table[N])