import sys
from collections import deque
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

zip_arr = list(zip(*arr))
new_arr = [[0 for _ in range(M)] for _ in range(N)]
for i in range(min(N, M)//2):
    q = deque()
    q.extend(arr[i][i:M-i])
    q.extend(zip_arr[M-i-1][i+1:N-i-1])
    q.extend(arr[-i-1][M-i-1:i:-1])
    q.extend(zip_arr[i][N-1-i:i:-1])
    q.rotate(-R)

    for j in range(i, M-i):
        new_arr[i][j] = q.popleft()
    for j in range(i+1, N-i-1):
        new_arr[j][M-i-1] = q.popleft()
    for j in range(M-i-1, i, -1):
        new_arr[-i-1][j] = q.popleft()
    for j in range(N-i-1, i, -1):
        new_arr[j][i] = q.popleft()

for i in new_arr:
    print(*i)