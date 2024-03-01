import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

R, C, K = map(int, input().split())
arr = []
for _ in range(R):
    line = list(input().rstrip())
    arr.append(line)

answer = 0
visited = [[0 for _ in range(C)] for _ in range(R)]
visited[R-1][0] = 1
def dfs(n, m, sm):
    global answer

    if n == 0 and m == C-1:
        if sm == K:
            answer += 1
        return

    for x, y in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
        nx = n + x
        my = m + y
        if 0 <= nx < R and 0 <= my < C:
            if arr[nx][my] != 'T' and visited[nx][my] == 0:
                visited[nx][my] = 1
                dfs(nx, my, sm+1)
                visited[nx][my] = 0

dfs(R-1, 0, 1)
print(answer)
