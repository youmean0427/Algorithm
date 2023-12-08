import sys
input = sys.stdin.readline

M = int(input())
N = int(input())

def find(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1

    if cnt == 2:
        return True
    else:
        return False

total = []
for i in range(M, N+1):
    if find(i):
        total.append(i)

if total:
    print(sum(total))
    print(total[0])
else:
    print(-1)
