import sys
from collections import deque
# sys.stdin = open('EX.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list([int(char) for char in input().split()] for _ in range(M))

q = deque([])
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            q.append((i, j))


while q:

    x, y = q.popleft()

    for n, m in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nx = x + n
        my = y + m
        if 0 <= nx < M and 0 <= my < N:
            if arr[nx][my] != -1:
                if arr[nx][my] == 0 or arr[nx][my] > arr[x][y] + 1 :
                    arr[nx][my] = arr[x][y] + 1
                    q.append((nx,my))

result = 0
# print(arr)
for j in arr:
    if 0 in j:
        result = 0
        break
    else:
        for k in j:
            if k > result:
                result = k

print(result - 1)