import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
bnt = [int(i) for i in input().split()]

ans = abs(N-100)

for i in range(1000001):
    i = str(i)

    for j in range(len(i)):
        if int(i[j]) in bnt:
            break
    else:
        ans = min(ans, abs(int(i)-N) + len(i))

print(ans)