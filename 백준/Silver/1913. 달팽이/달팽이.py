import sys
input = sys.stdin.readline

N = int(input())
find = int(input())

arr = [[0] * N for _ in range(N)]

count = 1
num = N//2
x, y = 0, 0

while count <= N ** 2:

    for i in range(num, N-num-1):
        arr[num][i+1] = count
        if count == find:
            x, y, = num, i+1
        count += 1

    for i in range(num+1, N-num-1):
        arr[i][N-num-1] = count
        if count == find:
            x, y, = i, N-num-1
        count += 1

    for i in range(N-num-1, num-1, -1):
        arr[N-num-1][i] = count
        if count == find:
            x, y, = N-num-1, i
        count += 1

    for i in range(N-num-2, num-1, -1):
        arr[i][num] = count
        if count == find:
            x, y, = i, num
        count += 1
    num -= 1

for i in arr:
    print(*i)
print(x+1, y+1)
