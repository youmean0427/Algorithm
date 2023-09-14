import sys
input = sys.stdin.readline

N = int(input())
map = input().rstrip()
arr = []

for i in map:
    arr.append(i)

visited = [0] * N
cnt = 0

for k in range(N):
    if visited[k] == 0:
        cnt += 1
        q = [k]
        visited[k] = cnt

        while q:

            a = q.pop(0)

            if arr[a] == 'E' and a + 1 < N:
                if visited[a+1] == 0:
                    visited[a+1] = cnt
                    q.append(a+1)
                else:
                    cnt = visited[a+1]
                    visited[a] = cnt

            elif arr[a] == 'W' and 0 <= a - 1:
                if visited[a-1] == 0:
                    visited[a-1] = cnt
                    q.append(a-1)
                else:
                    cnt = visited[a-1]
                    visited[a] = cnt

print(cnt)
