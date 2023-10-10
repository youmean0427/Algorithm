import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = int((Y * 100 / X))

start = 0
end = 1000000000
z = 0
result = -1

while start <= end:

    mid = (start + end) // 2

    if Z < int(((Y + mid) * 100 / (X + mid))):
        result = mid
        end = mid - 1
    else:
        start = mid + 1


if Z >= 99:
    print(-1)
else:
    print(result)