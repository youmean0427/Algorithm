import sys

# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

A, B, N, M = map(int, input().split())

max_val = max(A, B)
visited = [float('inf') for _ in range(100001)]


def bfs(start):
    q = [(start, 0)]

    while q:
        x, cnt = q.pop(0)
        if x == M:
            print(cnt)
            return

        if 0 <= x + 1 <= 100000:
            if visited[x + 1] > cnt + 1:
                visited[x + 1] = cnt + 1
                q.append((x + 1, cnt + 1))
        if 0 <= x - 1 <= 100000:
            if visited[x - 1] > cnt + 1:
                visited[x - 1] = cnt + 1
                q.append((x - 1, cnt + 1))
        if 0 <= x + A <= 100000:
            if visited[x + A] > cnt + 1:
                visited[x + A] = cnt + 1
                q.append((x + A, cnt + 1))
        if 0 <= x - A <= 100000:
            if visited[x - A] > cnt + 1:
                visited[x - A] = cnt + 1
                q.append((x - A, cnt + 1))
        if 0 <= x + B <= 100000:
            if visited[x + B] > cnt + 1:
                visited[x + B] = cnt + 1
                q.append((x + B, cnt + 1))
        if 0 <= x - B <= 100000:
            if visited[x - B] > cnt + 1:
                visited[x - B] = cnt + 1
                q.append((x - B, cnt + 1))
        if 0 <= x * A <= 100000:
            if visited[x * A] > cnt + 1:
                visited[x * A] = cnt + 1
                q.append((x * A, cnt + 1))
        if 0 <= x * B <= 100000:
            if visited[x * B] > cnt + 1:
                visited[x * B] = cnt + 1
                q.append((x * B, cnt + 1))


bfs(N)
