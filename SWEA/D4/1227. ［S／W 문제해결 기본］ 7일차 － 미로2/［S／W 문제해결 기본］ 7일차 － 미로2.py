def dfs(start):
    stack = [start]

    while stack:
        x, y = stack.pop()

        if visited[x][y] == 0:
            visited[x][y] = 1
            dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for n, m in dir:
                xn = x + n
                ym = y + m

                if 0 <= xn < 100 and 0 <= ym < 100:
                    if visited[xn][ym] == 0 and arr[xn][ym] == '0':
                        stack.append((xn, ym))
                    if arr[xn][ym] == '3':
                        return True

    return False

for _ in range(10):
    T = int(input())
    visited = [[0 for _ in range(100)] for _ in range(100)]
    arr = []

    for i in range(100):
        x = list(input())
        for j in range(100):
            if x[j] == '2':
                start = [i, j]
        arr.append(x)

    if dfs(start):
        print(f'#{T} 1')
    else:
        print(f'#{T} 0')