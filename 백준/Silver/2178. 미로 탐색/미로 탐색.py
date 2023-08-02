import sys
# sys.stdin = open('EX.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list([int(char) for char in input().rstrip()] for _ in range(N))

# print(arr)

q = [(0, 0)]
end = [N-1, M-1]
visited = [[0] * M for _ in range(N)]
count = 0

while q:
    # print(q)

    x, y = q.pop(0)
    visited[x][y] = 1
    count += 1

    if x == end[0] and y == end[1]:
        break

    for nx, ny in ([-1, 0], [0, 1], [1, 0], [0, -1]):
        if 0 <= x + nx < N and 0 <= y + ny < M:
            if arr[x+nx][y+ny] == 1:
                if visited[x+nx][y+ny] == 0:
                    q.append((x+nx, y+ny))
                    arr[x+nx][y+ny] = arr[x][y] + 1
                    visited[x][y] = 1

# print(arr)
print(arr[N-1][M-1])
