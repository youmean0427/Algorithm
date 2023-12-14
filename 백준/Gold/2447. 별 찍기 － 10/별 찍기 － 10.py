import sys, math
input = sys.stdin.readline

N = int(input())
arr = [["*"] * N for _ in range(N)]

def star(x, start, end, N):
    if N >= 3:
        for i in range(start+N//3, (start+N//3)+N//3):
            for j in range(end+N//3, (end + N//3)+N//3):
                x[i][j] = " "

        for n in range(start, start+N, N//3):
            for m in range(end, end+N, N//3):
                star(x, n, m, N//3)

star(arr, 0, 0, N)
for i in arr:
    print("".join(i))