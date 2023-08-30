import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

light = [int(x) for x in input().split()]
height = light[0]

for i in range(M-1):
    cnt = (light[i + 1] - light[i])

    if cnt % 2 == 0:
        cnt = cnt // 2
    else:
        cnt = (cnt // 2) + 1

    height = max(height, cnt)

height = max(height, N-light[-1])
print(height)