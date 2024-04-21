def solution(n):
    answer = []
    arr = [[0 for _ in range(n)] for _ in range(n)]
    start = (0, 0)
    exit = 0
    for i in range(1, n+1):
        exit += i

    def dfs(start):

        stack = [start]

        dir = [(1, 0), (0, 1), (-1, -1)]
        dir_idx = 0
        now_dir = dir[dir_idx]
        change_dir = {0: 1, 1: 2, 2: 0}
        arr[start[0]][start[1]] = 1

        while stack:
            x, y = stack.pop()

            if arr[x][y] == exit:
                return

            dn, dm = now_dir[0], now_dir[1]
            dnx, dmy = dn + x, dm + y
            if 0 <= dnx < n and 0 <= dmy < n:
                if arr[dnx][dmy] == 0:
                    arr[dnx][dmy] = arr[x][y] + 1
                    stack.append((dnx, dmy))
                    continue

            dir_idx = change_dir[dir_idx]
            now_dir = dir[dir_idx]
            stack.append((x, y))

    dfs(start)

    for i in arr:
        for k in i:
            if k != 0:
                answer.append(k)

    return answer