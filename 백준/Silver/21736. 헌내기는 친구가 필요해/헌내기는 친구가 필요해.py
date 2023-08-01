import sys
# sys.stdin = open('EX.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list([char for char in input().rstrip()] for _ in range(N))

for k in range(N):
    if 'I' in arr[k]:
        y = arr[k].index('I')
        break

I_index = (k, y)
q = [I_index]
visited=[[0] * M for _ in range(N)]
result = 0

while q:
    # print( q)
    now = q.pop()
    x, y = now[0], now[1]

    if visited[x][y] == 0:
        visited[x][y] = 1
    # print(visited)
    for nx, ny in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= x+nx < N and 0 <= y+ny < M:
            if arr[x+nx][y+ny] != 'X':
                if arr[x+nx][y+ny] == 'O':
                    if visited[x+nx][y+ny] == 0:
                        q.append((x+nx, y+ny))
                        visited[x+nx][y+ny] = 1


                elif arr[x+nx][y+ny] == 'P':
                    if visited[x + nx][y + ny] == 0:
                        result += 1
                        q.append((x + nx, y + ny))
                        visited[x + nx][y + ny] = 1

if result > 0:
    print(result)
else:
    print('TT')