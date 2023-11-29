import sys
input = sys.stdin.readline

N = int(input())
arr = [[] * N for _ in range(N)]
node = [int(i) for i in input().split()]

for i in range(len(node)):
    if node[i] != -1:
        arr[node[i]].append(i)
    else:
        start = i

del_node = int(input())

# DFS
cnt = 0
stack = [start]
visited = [0] * N
while stack:
    x = stack.pop()

    if x == del_node:
        continue

    if visited[x] == 0:
        visited[x] = 1

        if arr[x]:
            if del_node in arr[x] and len(arr[x]) == 1:
                cnt += 1
                break
            for i in arr[x][::-1]:
                stack.append(i)
        else:
            cnt += 1

print(cnt)