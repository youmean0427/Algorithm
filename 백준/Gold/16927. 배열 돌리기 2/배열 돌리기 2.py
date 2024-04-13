import sys
from collections import deque
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

min_val = min(N, M)
idx = 0
new_arr = [[0] * M for _ in range(N)]
while idx < min_val // 2:
    dq = deque()
    dq.extend(arr[idx][idx:M-idx])
    for i in arr[idx+1:N-idx]:
        dq.append(i[M-idx-1])
    dq.extend(arr[N-idx-1][M-idx-2:idx:-1])
    for i in arr[N-idx-1:idx:-1]:
        dq.append(i[idx])

    dq.rotate(-R)

    for i in range(idx, M-idx):
        new_arr[idx][i] = dq.popleft()
    for i in range(idx+1, N-idx-1):
        new_arr[i][M-idx-1] = dq.popleft()
    for i in range(M-idx-1, idx, -1):
        new_arr[-idx-1][i] = dq.popleft()
    for i in range(N-idx-1, idx, -1):
        new_arr[i][idx] = dq.popleft()
    idx += 1

for i in new_arr:
    print(*i)
