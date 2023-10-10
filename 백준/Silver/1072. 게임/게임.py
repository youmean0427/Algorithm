import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
# 부동소수점 오차, int(Y/X*100)으로 작성 금지!!!
Z = int((Y * 100 / X))

start = 0
end = X  # Y의 범위 : 0 <= Y <= X
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