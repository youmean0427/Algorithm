import sys
from collections import deque
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

arr = []
for _ in range(4):
    arr.append(deque(list(map(int, input().rstrip()))))

def dfs(start, dir):
    visited = [0] * 4
    q = [(start, dir)]
    clock = {1: -1, -1: 1}
    while q:
        now, d = q.pop()
        right = now + 1
        left = now - 1

        if visited[now] == 0:
            visited[now] = 1
            if 0 <= right < 4 :
                if arr[now][2] != arr[right][6]:
                    q.append((right, clock[d]))

            if 0 <= left < 4:
                if arr[now][6] != arr[left][2]:
                    q.append((left, clock[d]))
            arr[now].rotate(d)

T = int(input())
for _ in range(T):
    idx, dir = map(int, input().split())
    dfs(idx-1, dir)

ans, val = 0, 1
for i in range(4):
    ans += arr[i][0] * val
    val *= 2
print(ans)
