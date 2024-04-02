import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input().rstrip()))

def find_heart():
    for n in range(N):
        for m in range(N):
            if arr[n][m] == "*":
                heart = [n+2, m+1]
                return heart

def bfs(sx, sy):
    global mid
    q = [(sx, sy)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[sx-1][sy] = 1
    visited[sx][sy] = 1

    while q:

        x, y = q.pop(0)

        dir = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1)]
        check = 0

        for n, m in dir:
            nx = n + x
            my = m + y
            if 0 <= nx < N and 0 <= my < N:
                if visited[nx][my] == 0 and arr[nx][my] == "*":
                    visited[nx][my] += visited[x][y] + 1
                    q.append((nx, my))
                    check += 1
                    if n == m or n == -m:
                        mid = [x, y]

        if check == 0:
            pos.append((x, y))

    return visited


mid = []
pos = []
sx, sy = find_heart()
visited = bfs(sx-1, sy-1)
ans = [0] * 5

pos.sort(key=lambda x: (x[0], x[1]))
left_hand = pos.pop(0)
right_hand = pos.pop(0)

ans[0] = visited[left_hand[0]][left_hand[1]] - 1
ans[1] = visited[right_hand[0]][right_hand[1]] - 1
ans[2] = visited[mid[0]][mid[1]] - 1

pos.sort(key=lambda x: (x[1], x[0]))
left_leg = pos.pop(0)
right_leg = pos.pop(0)

ans[3] = visited[left_leg[0]][left_leg[1]] - ans[2] - 1
ans[4] = visited[right_leg[0]][right_leg[1]] - ans[2] - 1

print(sx, sy)
print(*ans)