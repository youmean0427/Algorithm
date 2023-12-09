import sys
input = sys.stdin.readline

N = int(input())
x = []
y = []
if N > 1:
    for _ in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    result = (max(x) - min(x)) * (max(y) - min(y))
    print(result)

else:
    print(0)