def solution(n, wires):
    global answer
    
    def dfs(start, area):

        stack = [start]
        visited[start] = area

        while stack:
            x = stack.pop(0)

            for i in arr[x]:
                if visited[i] == 0:
                    visited[i] = visited[x]
                    stack.append(i)

    def make_arr():
        arr = [[] for _ in range(n + 1)]

        for a, b in wires:
            if temp == [a, b]:
                continue
            arr[a].append(b)
            arr[b].append(a)

        return arr

    def count_area(visited):
        area_cnt = {}
        for k in visited[1:]:
            if k in area_cnt:
                area_cnt[k] += 1
            else:
                area_cnt[k] = 0
        return area_cnt

    def find_answer(area_cnt):
        global answer

        value = [0, 0]
        for idx, item in enumerate(area_cnt.values()):
            value[idx] = item

        answer = min(answer, abs(value[1] - value[0]))
        return answer

    i = 0
    answer = 100

    while i < len(wires):
        temp = wires[i]
        arr = make_arr()

        visited = [0] * (n + 1)
        area = 1

        for j in range(1, n + 1):
            if visited[j] == 0:
                dfs(j, area)
                area += 1

        area_cnt = count_area(visited)
        answer = find_answer(area_cnt)

        i += 1

    return answer