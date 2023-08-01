import sys
# sys.stdin = open('EX.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

def bfs():
    for k in range(N):
        if 'I' in arr[k]:
            y = arr[k].index('I')
            break

    I_index = (k, y)
    q = [I_index]
    visited = [[0] * M for _ in range(N)]
    result = 0

    while q:
        now = q.pop(0)
        x, y = now[0], now[1]

        if arr[x][y] == 'P':
            result += 1

        visited[x][y] = 1

        for nx, ny in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 <= x + nx < N and 0 <= y + ny < M:
                if arr[x + nx][y + ny] != 'X' and not visited[x + nx][y + ny]:
                    q.append((x + nx, y + ny))
                    visited[x + nx][y + ny] = 1

    return result

result = bfs()

if result > 0:
    print(result)
else:
    print('TT')