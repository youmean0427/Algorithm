import sys
input = sys.stdin.readline

N = int(input())
q = list(int(x) for x in input().split())
result = []

while q:

    x = q.pop(0)

    if x == 0:
        result.append(0)
        continue

    if result:
        if result[-1] != 0:
            result.append(x + result[-1])
        else:
            result.append(x)
    else:
        result.append(x)

print(sum(result))

