import sys
input = sys.stdin.readline

N = int(input())
arr = [[x for x in input().split()] for _ in range(N)]
visited = [[set() for _ in range(N)] for _ in range(N)]
visited[0][0].add(int(arr[0][0]))

def bfs(arr, start, end):

    q = [(start, end)]

    while q:

        x, y = q.pop(0)
        dir = [(0, 1), (1, 0)]
        dir_2 = [(0, -2), (-1, -1), (-2, 0)]
        for n, m in dir:
            nx = n + x
            my = m + y

            if 0 <= nx < N and 0 <= my < N:
                if arr[nx][my].isdigit():
                    if nx == x:
                        dir_start, dir_end = 0, 2
                    else:
                        dir_start, dir_end = 1, 3
                        
                    for a, b in dir_2[dir_start:dir_end]:
                        if 0 <= a + nx < N and 0 <= b + my < N:
                            if visited[a + nx][b + my]:
                                if arr[x][y] == '+':
                                    visited[nx][my].add(min(visited[a+nx][b+my]) + int(arr[nx][my]))
                                    visited[nx][my].add(max(visited[a+nx][b+my]) + int(arr[nx][my]))
                                elif arr[x][y] == '-':
                                    visited[nx][my].add(min(visited[a+nx][b+my]) - int(arr[nx][my]))
                                    visited[nx][my].add(max(visited[a+nx][b+my]) - int(arr[nx][my]))
                                elif arr[x][y] == '*':
                                    visited[nx][my].add(min(visited[a+nx][b+my]) * int(arr[nx][my]))
                                    visited[nx][my].add(max(visited[a+nx][b+my]) * int(arr[nx][my]))

                    q.append((nx, my))
                else:
                    q.append((nx, my))

bfs(arr, 0, 0)
print(max(visited[-1][-1]), min(visited[-1][-1]))