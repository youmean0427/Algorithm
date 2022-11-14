T = int(input())

def DFS(n):
    global result
    count = 0
    while stack:
        # print(stack)
        k = stack.pop()

        if visited[arr[k]] == 1 and arr[k] == n:
            result += 1
            return
        if visited[arr[k]] == 1 and count == 0:
            return

        if visited[arr[k]] == 0:
            visited[arr[k]] = 1
            stack.append(arr[k])
            count += 1
        elif visited[arr[k]] == 1:
            result += 1
            return


for i in range(T):
    N = int(input())
    arr = [0] * (N+1)
    visited = [0] * (N+1)
    num = list(map(int, input().split()))

    for i in range(1, len(arr)):
        arr[i] = num[i-1]
    # print(arr)

    result = 0


    for i in range(1, len(arr)):
        stack = [i]
        visited[i] = 1
        DFS(i)
    print(result)