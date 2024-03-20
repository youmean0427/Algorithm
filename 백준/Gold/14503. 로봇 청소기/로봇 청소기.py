import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

# 0 : 상, 1: 우, 2: 하, 3: 좌
N, M = map(int, input().split()) # 방의 크기
start = list(map(int, input().split())) # 좌표, 방향
room = []
robot = [[-1 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    room.append(list(map(int, input().split())))
robot[start[0]][start[1]] = start[2]
ans = 0

def clean(arr, x, y):
    global ans
    if arr[x][y] == 0:
        arr[x][y] = -1
        ans += 1
    return arr

def four_movement(arr, x, y): # arr은 room / x, y는 robot 좌표

    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for n, m in dir:
        nx, my = n + x, m + y
        if 0 <= nx < N and 0 <= my < M:
            if arr[nx][my] == 0:
                return True
    return False


def rotate(arr, x, y, d):
    four = {1: 0, 0: 3, 3: 2, 2: 1}
    robot[x][y] = four[d]
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    n, m = dir[robot[x][y]]
    nx, my = n + x, m + y
    if 0 <= nx < N and 0 <= my < M:
        if arr[nx][my] == 0:
            robot[nx][my] = robot[x][y]
            robot[x][y] = -1
            return (nx, my)
    return (x, y)

def can_back(arr, x, y):
    four = {0: 2, 2: 0, 1: 3, 3: 1}
    back_dir = four[robot[x][y]]
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    n, m = dir[back_dir]
    nx, my = n + x, m + y
    if 0 <= nx < N and 0 <= my < M:
        if arr[nx][my] != 1:
            return True
    return False

def go_back(arr, x, y):
    four = {0: 2, 2: 0, 1: 3, 3: 1}
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    back_dir = four[robot[x][y]]
    n, m  = dir[back_dir]
    robot[n+x][m+y] = robot[x][y]
    robot[x][y] = -1
    return (n+x, m+y)

sx = start[0]
sy = start[1]

while True:
    room = clean(room, sx, sy)
    if four_movement(room, sx, sy):
        sx, sy = rotate(room, sx, sy, robot[sx][sy])
    else:
        if can_back(room, sx, sy):
            sx, sy = go_back(room, sx, sy)
        else:
            print(ans)
            exit(0)
