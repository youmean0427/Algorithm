arr = [[0] * 100 for _ in range(100)]

N = int(input())
for i in range(N):
    x, y = map(int, input().split())

    for k in range(x, x+10):
        for j in range(y, y+10):
            # print(k, j)
            arr[k][j] = 1

final = 0
for m in arr:
    final += m.count(1)

print(final)