import sys

# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
ans = 0
for _ in range(N):
    arr.append(list(map(int, input().split())))

blue = [[(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)]]
yellow = [[(0, 1), (1, 0), (1, 1)]]
orange = [
    [(0, 1), (0, 2), (-1, 2)], [(0, 1), (0, 2), (1, 2)],
    [(1, 0), (2, 0), (2, -1)], [(1, 0), (2, 0), (2, 1)],
    [(-1, 0), (-2, 0), (-2, 1)], [(-1, 0), (-2, 0), (-2, -1)],
    [(0, -1), (0, -2), (1, -2)], [(0, -1), (0, -2), (-1, -2)]
]
green = [
    [(0, 1), (-1, 1), (-1, 2)], [(0, 1), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (2, 1)], [(1, 0), (1, -1), (2, -1)]
]
pink = [
    [(0, 1), (0, 2), (-1, 1)], [(0, 1), (0, 2), (1, 1)],
    [(1, 0), (2, 0), (1, 1)], [(1, 0), (2, 0), (1, -1)]
]

tet = blue + yellow + orange + green + pink
ans = 0


def block(x, y, t):
    global ans
    total = arr[x][y]

    for bn, bm in t:
        if 0 <= x + bn < N and 0 <= y + bm < M:
            total += arr[x + bn][y + bm]

        else:
            return

    ans = max(ans, total)
    return


def find(x, y):
    for t in tet:
        block(x, y, t)


for n in range(N):
    for m in range(M):
        find(n, m)

print(ans)
